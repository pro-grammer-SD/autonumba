import ast

class Injector(ast.NodeTransformer):
    def __init__(self, deco, src_lines):
        self.deco = deco
        self.src_lines = src_lines
        self.changed = False

    def visit_FunctionDef(self, node):
        # Check if the original line contains '#nonumba'
        if "#nonumba" in self.src_lines[node.lineno - 1]:
            return node

        for d in node.decorator_list:
            if isinstance(d, ast.Call) and getattr(d.func, "id", None) == "njit":
                return node
        node.decorator_list.insert(0, self.deco)
        self.changed = True
        return node

def make_decorator(opts):
    kws = [ast.keyword(arg=k, value=ast.Constant(True)) for k, v in opts.items() if v]
    return ast.Call(func=ast.Name(id="njit"), args=[], keywords=kws)

def boost_file(path, opts, inplace):
    src = path.read_text(encoding="utf8")
    lines = src.splitlines()
    tree = ast.parse(src)
    deco = make_decorator(opts)
    inj = Injector(deco, lines)
    tree = inj.visit(tree)
    if not inj.changed:
        return

    preamble = (
        "from numba import njit\n"
        "import warnings\n"
        "from numba.core.errors import NumbaPerformanceWarning\n"
        "warnings.simplefilter('ignore', category=NumbaPerformanceWarning)\n\n"
    )

    out = preamble + ast.unparse(tree)

    if inplace:
        path.write_text(out, encoding="utf8")
    else:
        new_path = path.with_name(path.stem + "_autonumba.py")
        new_path.write_text(out, encoding="utf8")
        