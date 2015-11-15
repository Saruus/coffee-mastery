# coffee-mastery
CoffeeScript Mastery program
============================

This is a Python script that analyzes CoffeeScript programs to see the programming
mastery level of the programer. It is intended to measure the development
of computational thinking of a CoffeeScript learner by assessing programming
structures and elements in the code.

It has been developed as part of the <a href="https://github.com/gregoriorobles/drPencilcode">drPencilcode</a> platform.

This project is based on the <a href="https://github.com/jemole/hairball/blob/master/hairball/plugins/mastery.py">Mastery</a> plug-in by <a href="https://github.com/jemole">Jesús Moreno León</a> for <a href="https://github.com/ucsb-cs-education/hairball">Hairball</a>. All compliments should go to him, all complaints are without doubt my fault.

The current status of this project is alpha. Please, use it with this in mind.

Usage
=====

python coffee-mastery.py filename.coffee

Requirements
============

* Python
* coffee-mastery
* <a href="https://github.com/mdiebolt/clog">clog</a>
  * exec-sync (npm install exec-sync)
  * minimist (npm install minimist)
