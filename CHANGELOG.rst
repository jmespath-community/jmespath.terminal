1.1.1
=====

* Updated dependencies

1.1.0
=====

* JEP-11 Lexical Scoping
* JEP-13 Object Manipulation functions
* JEP-14 String functions
* JEP-15 String Slices
* JEP-16 Arithmetic Expressions
* JEP-17 Root Reference
* JEP-18 Grouping
* JEP-19 Evaluation of Pipe Expressions
  (`discussion #113 <https://github.com/jmespath-community/jmespath.spec/discussions/113>`__)

0.2.2
=====

* Use OrderedDict to retain key order from expression
  in output.

0.2.1
=====

* Add an ``-o|--output-file`` option that allows you to
  control where the final output is written.
* Relax pygments version constraint.

0.2.0
=====

* Backwards incompatible: Ctrl-p has been changed to now
  be an output mode toggle.  The output mode tells jpterm
  what to print (if anything) when it exits.  You can now
  no longer save and print multiple expressions.
* You can now exit jpterm using ctrl-c in addition to
  F5.  This fixes issues for people that were unable to
  use F5 previously.

0.1.0
=====

* Add support for reading the input JSON document from stdin.
  This also changes the -i option to a positional argument.
* Rename main executable from jmespath-term to jpterm.
