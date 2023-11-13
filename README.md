# Reproduce mypy 1.7 crash
1. Create clean Python 3.10 environment
2. [Install mypy from source](https://mypy.readthedocs.io/en/stable/common_issues.html#using-a-development-mypy-build) (reproduced with efa5dcb35)
3. Install this package: `pip install -e .`
4. Run mypy: `mypy . --show-traceback`

Output:
```text
Traceback (most recent call last):
  File "/home/mertschn/.conda/envs/mypy-repro/bin/mypy", line 8, in <module>
    sys.exit(console_entry())
  File "/home/mertschn/.conda/envs/mypy-repro/lib/python3.10/site-packages/mypy/__main__.py", line 15, in console_entry
    main()
  File "/home/mertschn/.conda/envs/mypy-repro/lib/python3.10/site-packages/mypy/main.py", line 100, in main
    res, messages, blockers = run_build(sources, options, fscache, t0, stdout, stderr)
  File "/home/mertschn/.conda/envs/mypy-repro/lib/python3.10/site-packages/mypy/main.py", line 182, in run_build
    res = build.build(sources, options, None, flush_errors, fscache, stdout, stderr)
  File "/home/mertschn/.conda/envs/mypy-repro/lib/python3.10/site-packages/mypy/build.py", line 191, in build
    result = _build(
  File "/home/mertschn/.conda/envs/mypy-repro/lib/python3.10/site-packages/mypy/build.py", line 265, in _build
    graph = dispatch(sources, manager, stdout)
  File "/home/mertschn/.conda/envs/mypy-repro/lib/python3.10/site-packages/mypy/build.py", line 2943, in dispatch
    process_graph(graph, manager)
  File "/home/mertschn/.conda/envs/mypy-repro/lib/python3.10/site-packages/mypy/build.py", line 3341, in process_graph
    process_stale_scc(graph, scc, manager)
  File "/home/mertschn/.conda/envs/mypy-repro/lib/python3.10/site-packages/mypy/build.py", line 3442, in process_stale_scc
    graph[id].type_check_first_pass()
  File "/home/mertschn/.conda/envs/mypy-repro/lib/python3.10/site-packages/mypy/build.py", line 2311, in type_check_first_pass
    self.type_checker().check_first_pass()
  File "/home/mertschn/.conda/envs/mypy-repro/lib/python3.10/site-packages/mypy/checker.py", line 481, in check_first_pass
    self.accept(d)
  File "/home/mertschn/.conda/envs/mypy-repro/lib/python3.10/site-packages/mypy/checker.py", line 591, in accept
    stmt.accept(self)
  File "/home/mertschn/.conda/envs/mypy-repro/lib/python3.10/site-packages/mypy/nodes.py", line 787, in accept
    return visitor.visit_func_def(self)
  File "/home/mertschn/.conda/envs/mypy-repro/lib/python3.10/site-packages/mypy/checker.py", line 1000, in visit_func_def
    self._visit_func_def(defn)
  File "/home/mertschn/.conda/envs/mypy-repro/lib/python3.10/site-packages/mypy/checker.py", line 1004, in _visit_func_def
    self.check_func_item(defn, name=defn.name)
  File "/home/mertschn/.conda/envs/mypy-repro/lib/python3.10/site-packages/mypy/checker.py", line 1077, in check_func_item
    self.check_func_def(defn, typ, name, allow_empty)
  File "/home/mertschn/.conda/envs/mypy-repro/lib/python3.10/site-packages/mypy/checker.py", line 1293, in check_func_def
    self.accept(item.body)
  File "/home/mertschn/.conda/envs/mypy-repro/lib/python3.10/site-packages/mypy/checker.py", line 591, in accept
    stmt.accept(self)
  File "/home/mertschn/.conda/envs/mypy-repro/lib/python3.10/site-packages/mypy/nodes.py", line 1223, in accept
    return visitor.visit_block(self)
  File "/home/mertschn/.conda/envs/mypy-repro/lib/python3.10/site-packages/mypy/checker.py", line 2770, in visit_block
    self.accept(s)
  File "/home/mertschn/.conda/envs/mypy-repro/lib/python3.10/site-packages/mypy/checker.py", line 591, in accept
    stmt.accept(self)
  File "/home/mertschn/.conda/envs/mypy-repro/lib/python3.10/site-packages/mypy/nodes.py", line 1436, in accept
    return visitor.visit_assert_stmt(self)
  File "/home/mertschn/.conda/envs/mypy-repro/lib/python3.10/site-packages/mypy/checker.py", line 4565, in visit_assert_stmt
    self.expr_checker.accept(s.expr)
  File "/home/mertschn/.conda/envs/mypy-repro/lib/python3.10/site-packages/mypy/checkexpr.py", line 5716, in accept
    typ = node.accept(self)
  File "/home/mertschn/.conda/envs/mypy-repro/lib/python3.10/site-packages/mypy/nodes.py", line 2076, in accept
    return visitor.visit_comparison_expr(self)
  File "/home/mertschn/.conda/envs/mypy-repro/lib/python3.10/site-packages/mypy/checkexpr.py", line 3573, in visit_comparison_expr
    if self.dangerous_comparison(left_type, right_type):
  File "/home/mertschn/.conda/envs/mypy-repro/lib/python3.10/site-packages/mypy/checkexpr.py", line 3705, in dangerous_comparison
    ) or self.dangerous_comparison(left.args[1], right.args[1])
  File "/home/mertschn/.conda/envs/mypy-repro/lib/python3.10/site-packages/mypy/checkexpr.py", line 3705, in dangerous_comparison
    ) or self.dangerous_comparison(left.args[1], right.args[1])
  File "/home/mertschn/.conda/envs/mypy-repro/lib/python3.10/site-packages/mypy/checkexpr.py", line 3705, in dangerous_comparison
    ) or self.dangerous_comparison(left.args[1], right.args[1])
  [Previous line repeated 16340 more times]
  File "/home/mertschn/.conda/envs/mypy-repro/lib/python3.10/site-packages/mypy/checkexpr.py", line 3701, in dangerous_comparison
    left = map_instance_to_supertype(left, abstract_map)
  File "/home/mertschn/.conda/envs/mypy-repro/lib/python3.10/site-packages/mypy/maptype.py", line 42, in map_instance_to_supertype
    return map_instance_to_supertypes(instance, superclass)[0]
  File "/home/mertschn/.conda/envs/mypy-repro/lib/python3.10/site-packages/mypy/maptype.py", line 54, in map_instance_to_supertypes
    a.extend(map_instance_to_direct_supertypes(t, sup))
  File "/home/mertschn/.conda/envs/mypy-repro/lib/python3.10/site-packages/mypy/maptype.py", line 96, in map_instance_to_direct_supertypes
    t = expand_type_by_instance(b, instance)
  File "/home/mertschn/.conda/envs/mypy-repro/lib/python3.10/site-packages/mypy/expandtype.py", line 119, in expand_type_by_instance
    return expand_type(typ, variables)
  File "/home/mertschn/.conda/envs/mypy-repro/lib/python3.10/site-packages/mypy/expandtype.py", line 71, in expand_type
    return typ.accept(ExpandTypeVisitor(env))
  File "/home/mertschn/.conda/envs/mypy-repro/lib/python3.10/site-packages/mypy/types.py", line 1435, in accept
    return visitor.visit_instance(self)
  File "/home/mertschn/.conda/envs/mypy-repro/lib/python3.10/site-packages/mypy/expandtype.py", line 214, in visit_instance
    args = self.expand_types_with_unpack(list(t.args))
  File "/home/mertschn/.conda/envs/mypy-repro/lib/python3.10/site-packages/mypy/expandtype.py", line 396, in expand_types_with_unpack
    items.append(item.accept(self))
  File "/home/mertschn/.conda/envs/mypy-repro/lib/python3.10/site-packages/mypy/types.py", line 635, in accept
    return visitor.visit_type_var(self)
  File "/home/mertschn/.conda/envs/mypy-repro/lib/python3.10/site-packages/mypy/expandtype.py", line 234, in visit_type_var
    return repl.copy_modified(last_known_value=None)
  File "/home/mertschn/.conda/envs/mypy-repro/lib/python3.10/site-packages/mypy/types.py", line 1488, in copy_modified
    new = Instance(
  File "/home/mertschn/.conda/envs/mypy-repro/lib/python3.10/site-packages/mypy/types.py", line 1373, in __init__
    super().__init__(line, column)
  File "/home/mertschn/.conda/envs/mypy-repro/lib/python3.10/site-packages/mypy/types.py", line 234, in __init__
    super().__init__(line, column)
RecursionError: maximum recursion depth exceeded while calling a Python object
```