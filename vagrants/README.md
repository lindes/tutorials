<div id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#sec-1">1. Introduction</a></li>
<li><a href="#sec-2">2. Helpers before you get started</a>
<ul>
<li><a href="#sec-2-1">2.1. Creating a <code>subl</code> alias:</a></li>
</ul>
</li>
<li><a href="#sec-3">3. Specific Vagrant configurations:</a>
<ul>
<li><a href="#sec-3-1">3.1. React</a></li>
<li><a href="#sec-3-2">3.2. Rails</a></li>
<li><a href="#sec-3-3">3.3. Flask</a>
<ul>
<li><a href="#sec-3-3-1">3.3.1. python 2.7</a></li>
<li><a href="#sec-3-3-2">3.3.2. python 3</a></li>
<li><a href="#sec-3-3-3">3.3.3. more to come?</a></li>
</ul>
</li>
</ul>
</li>
</ul>
</div>
</div>



# Introduction<a id="sec-1" name="sec-1"></a>

This tree within the [tutorials](https://github.com/lindes/tutorials) I'm doing is meant to contain [Vagrant](https://www.vagrantup.com/)
configurations for various sorts of projects one might want to do, so
that one can get a quick start working on the core of a project,
without having to go through the (sometimes-easy,
sometimes-cumbersome) installation process.  (For the curious, you can
still inspect how things are done by looking at the "provisioning"
portions of the file.)

# Helpers before you get started<a id="sec-2" name="sec-2"></a>

## Creating a `subl` alias:<a id="sec-2-1" name="sec-2-1"></a>

If you don't already have a `subl` alias, try the following command:

ln -si "$(/bin/ls -1 /Applications/Sublime\ Text*.app/Contents/SharedSupport/bin/subl | tail -1)" /usr/local/bin

Hopefully that will do the trick; if it does not, there's more
information about creating the alias [on stackoverflow](https://stackoverflow.com/a/16495202/313756), just know that
sometimes it's something like `Sublime Text 2` or `Sublime Text 3`
instead of merely `Sublime Text`. You'll have to see what it is on the
system you're on; or feel free to ask.  Or just open Sublime first,
and open the directory you're in from there.

# Specific Vagrant configurations:<a id="sec-3" name="sec-3"></a>

## React<a id="sec-3-1" name="sec-3-1"></a>

Using the Vagrant file in the react/ subdirectory, use the following
steps.  Steps 1 and 2 are optional, but recommended:

1.  Copy the Vagrantfile into a directory (possibly creating it first)
where you intend to do the work of this project.
2.  If you haven't already, run `git init` there.  And `git add` the
Vagrantfile.  (`git commit` either now or later, as you prefer.)
3.  Run `vagrant up`.
4.  Wait.  :) *(But you can do step 5 from another shell while you
wait.)*
5.  Run `subl .`, just to open Sublime for the folder you're in.  (If
you don't already have the `subl` alias, you can create it or open
it differently; see instructions for that, above).  Once you've
open that, switch back to the shell for the next few steps.
6.  Run `vagrant ssh`.
7.  Move into the `src` directory (`cd src`).  This will be
automatically (according to the `synced_folder` directive that's in
the Vagrantfile) be synchronized with the directory on the
filesystem where Vagrantfile lives in the "host" computer (the Mac
or Windows box where you're running all this).
8.  Follow the [tic-tac-toe tutorial instructions](https://reactjs.org/tutorial/tutorial.html#if-you-prefer-to-write-code-in-your-editor), ***starting at step
2*** (you don't even need to read the text above that), but ignoring
the "installation instructions" link, as the commands right below
that on the page are all you'll need to do.
9.  Proceed from there!  (You can switch back and forth to Sublime to
edit files, as desired.)  Happy hacking!

## Rails<a id="sec-3-2" name="sec-3-2"></a>

[Instructions and Vagrantfile yet to be written.]

## Flask<a id="sec-3-3" name="sec-3-3"></a>

### python 2.7<a id="sec-3-3-1" name="sec-3-3-1"></a>

[Instructions and Vagrantfile yet to be written.]

### python 3<a id="sec-3-3-2" name="sec-3-3-2"></a>

[Instructions and Vagrantfile yet to be written.]

### more to come?<a id="sec-3-3-3" name="sec-3-3-3"></a>