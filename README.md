co.py.cat
=========

An implementation of [Douglas Hofstadter](http://prelectur.stanford.edu/lecturers/hofstadter/)'s copycat algorithm. The copycat algorithm is explained [on Wikipedia](https://en.wikipedia.org/wiki/Copycat_%28software%29), and that page has many links for deeper reading.

This implementation is a copycat of Scott Boland's [Java implementation](http://itee.uq.edu.au/~scottb/_Copycat/), but re-written into Python. It's not a direct translation - but based on his code. I did not carry over the GUI, as this version can more usefully be run from command line, or imported for use by other Python scripts, and GUIs restrict the platform too much.

In cases where I could not grok the Java implementation easily I took ideas from the [LISP implementation](http://web.cecs.pdx.edu/~mm/how-to-get-copycat.html), or directly from [Melanie Mitchell](https://en.wikipedia.org/wiki/Melanie_Mitchell)'s "[Analogy-Making as Perception](http://www.amazon.com/Analogy-Making-Perception-Computer-Melanie-Mitchell/dp/0262132893/ref=tmm_hrd_title_0?ie=UTF8&qid=1351269085&sr=1-3)"

I also tried to make the code "more pythonic".

Installation
------------

There are no particular installation instructions, just clone and run, e.g.

```sh
$ git clone https://github.com/jalanb/co.py.cat.git
$ cd co.py.cat/copycat
$ python3 -m copycat abc abd ijk
```

Running
-------

The script takes three arguments.
    The first two are a pair of triplets with some change, for example "abc" and "abd".
    The third is a triplet which the script should try to change analogously

For example the following invocation will probably display "ijl"

```sh
$ python main.py abc abd ijk
```

Links
=====

Readers who got this far will definitely enjoy analogising this project with @[Alex-Linhares](https://github.com/Alex-Linhares/co.py.cat)'s collection of FARGonautica over [yonder](https://github.com/Alex-Linhares/FARGonautica#projects-to-join-here-desiderata)

Thanks
======
A big "Thank You" for

Curation
--------
* @[Alex-Linhares](https://github.com/Alex-Linhares/FARGonautica#projects-to-join-here-desiderata)

Contributions
-------------
* @[Quuxplusone](https://github.com/jalanb/co.py.cat/pull/8) for reducing spew
* @[jtauber](https://github.com/jalanb/co.py.cat/pull/3) for cleaning up

Forks
-----
* @[Alex-Linhares](https://github.com/Alex-Linhares/co.py.cat)
* @[ayberkt](https://github.com/ayberkt/co.py.cat)
* @[dproske](https://github.com/dproske/co.py.cat)
* @[erkapilmehta](https://github.com/erkapilmehta/co.py.cat)
* @[horacio](https://github.com/horacio/co.py.cat)
* @[josephfosco](https://github.com/josephfosco/co.py.cat)
* @[jtauber](https://github.com/jtauber/co.py.cat)
* @[OrmesKD](https://github.com/OrmesKD/co.py.cat)
* @[Quuxplusone](https://github.com/Quuxplusone/co.py.cat)
* @[qython](https://github.com/qython/co.py.cat)
* @[sjolicoeur](https://github.com/sjolicoeur/co.py.cat)
* @[skaslev](https://github.com/skaslev/co.py.cat)

You geeks make it all so worthwhile.


Badges
------
[![Build Status](https://travis-ci.org/jalanb/co.py.cat.svg?branch=master)](https://travis-ci.org/jalanb/co.py.cat)

See Also
--------
1. "[The Copycat Project: An Experiment in Nondeterminism and Creative Analogies](http://dspace.mit.edu/handle/1721.1/5648)" by [Hofstadter, Douglas](https://en.wikipedia.org/wiki/Douglas_Hofstadter#Academic_career)
1. "[Analogy-Making as Perception](http://www.amazon.com/Analogy-Making-Perception-Computer-Melanie-Mitchell/dp/0262132893/ref=tmm_hrd_title_0?ie=UTF8&qid=1351269085&sr=1-3)" by [Mitchell, Melanie](https://en.wikipedia.org/wiki/Melanie_Mitchell)
1. The Fargonauts' "[FARGonautica](https://github.com/fargonauts/FARGonautica)", a curation of analogous projects by [Alex Linhares](https://github.com/Alex-Linhares)
1. Arthur O'Dwyer ([Quuxplusone on GitHub]()) has further cleaned and extended this code (including a GUI) in a fork available [here](https://github.com/Quuxplusone/co.py.cat).
