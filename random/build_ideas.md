[Note: this document can be found online at [bit.ly/hb-buildday-ideas](http://bit.ly/hb-buildday-ideas).]

# Application ideas!


Here are some ideas for projects one could build, with a description
of a basic Minimum Viable Product (MVP), plus varying components that
would add complexity, should you wish to take this app beyond MVP status.

It's totally OK to take these project ideas home with you!  Continue
work on what you start here today, or start another one; it's up to
you. :) And of course, you can also work on whatever projects you
already have ideas for, even if you've already started.  It's a day to
build, whatever and however you like, with the support of peers and
experienced supporters to ask questions of.

If you do finish an MVP and/or extra components today, *great*!  AND,
also know that it's totally fine to need more time.  Experience shows
that most folks do, so you won't be alone &#x2013; the few hours we have set
aside today are not a lot of time, especially if you're trying for
bonus components in the app you choose to build.

Also, for the purposes of today's exercise, having this be a
multi-user app (except in the case of the chat app) is considered a
bonus, rather than part of the MVP.  The idea is to have you build
something that does something in a way that can be used by *someone*.
Without supporting multiple accounts, most apps won't be "viable" in a
release-it-to-the-world way, but they sure will be for the purposes of
a learning exercise.  That said, it's recommended that you keep in
mind what would have to be different to make it multi-user if you
don't start out that way.  That way, it'll be easier to transition
later if/when you decide to.  Plus it's just a good thinking
exercise. 😊

Without further ado, here are a few app ideas, broken into categories:

## JavaScript-oriented projects:

### Tic Tac Toe (goal: build using React)

An app to do [tic-tac-toe](https://en.wikipedia.org/wiki/Tic-tac-toe) in the browser.  Note that there's a tutorial
for doing exactly this on the react web page:
[facebook.github.io/react/tutorial/tutorial.html](https://facebook.github.io/react/tutorial/tutorial.html)

Also, you may find this [Vagrant mini-guide written specifically for
this project](https://github.com/lindes/tutorials/tree/master/vagrants#react) (or even just the accompanying [Vagrantfile](https://raw.githubusercontent.com/lindes/tutorials/master/vagrants/react/Vagrantfile)) useful to get
the ball rolling.

#### MVP requirements

-   Display a 3x3 grid, with the characteristic "#" pattern.
-   when clicking on a square in the grid, change it to the current
player indicator &#x2013; either an X or an O.
-   toggle between X and O and the next play.

#### Bonus functionalities

-   have a server backend that allows two people to play against
each other, one getting X, and one getting O.  Keep track of
turns.  This could involve just sharing a special URL for the
game ID, or:
-   allow some form of login (could be ephemeral, could be
long-lasting), and for people to start games and wait for
another player to join them.
-   keep track of cumulative scores for a player (wins, losses,
draws)

### Display data on meteors (goal: build using D3)

Get data from an external source about meteors, and display a visual
representation of them using D3

#### MVP requirements

-   get the data [from NASA](https://data.nasa.gov/Space-Science/Meteorite-Landings/gh4g-9sfh) (clicking "Export" on the top-right and
choosing "CSV" is recommended; you can then decide a way to
convert and/or import the data so the app can use it.)
-   Make the data available &#x2013; two main options here:
-   on the backend &#x2013; create a model and import into a database
-   on the frontend &#x2013; convert the data into JSON or similar, so
you can fetch it
-   build some sort of visualization based on this data.  Ideas for
starting points on this:
-   build a scatter-plot of mass over time
-   plot the landings on a map.  ([d3-geo](https://github.com/d3/d3-geo) may be useful here.)

## Backend-oriented apps

For these, you could either continue to use Flask as a starting point,
or branch out into trying [Django](https://www.djangoproject.com/) (a popular Python-based framework) or
[Rails](http://rubyonrails.org/) (another popular framework, this one [Ruby](https://www.ruby-lang.org/)-based, thus exposing
you to not only a new framework, but a whole new programming
language).

### To-do list app

An app for keeping track of things one needs to do.

#### MVP requirements

-   Allow the entry of new items that might need doing.
-   Store such items in a database, so they can be retrieved later.
-   Present a list of stored items.
-   Have a way to mark an item completed.
-   When an item is marked completed, either alter the way it's
displayed (e.g. <del>strikethrough</del>), or simply remove it.

#### Bonus functionalities

Feel free to add any one or as many as you like of the following:

-   Provide a way to delete an item, instead of just completing it.
-   Allow a user to edit the description of an item.
-   Have accounts and login/logout, with items stored privately for each user.
-   slick AJAX-y interface, where items perhaps gradually fade from
screen, or get moved to a different part of the page showing
recently-completed items, or such.
-   an "undo" for completions or deletions.
-   due-dates for items
-   contexts for items (e.g. one item is something to buy at a grocery
store, and you'd only see it when looking at a grocery list; another
item is a phone call you need to make; and another is something you
have to do at home.)

### Search for events (such as Career Fairs) on Eventbrite (goal: build using Eventbrite API)

Something to look through Eventbrite events, and search for certain
kinds of events.

#### MVP requirements

-   connect with the [Eventbrite API](http://developer.eventbrite.com)
-   get a list of events
-   filter either or both of:
-   at the API level (e.g. using categories, keyword search, and/or
location searches)
-   within the app you're building (further filtering based on
some criteria you might have that the API doesn't fully
accommodate, or if you want to allow the user to dynamically
alter their search without making an API call each time.)

#### Bonus requirements

-   Allow a user to either select or dismiss events &#x2013; selected
events showing up in a list of things they want to go to,
dismissed events disappearing from the display, even if a new
search is done.

### Chat application between people

Allow people to chat via their browsers.

#### MVP requirements

-   Allow at least two people to connect to the website, with at
least a minimal login (could just be ephemeral &#x2013; e.g. "Enter
your name").
-   Have a way for two users to connect to each other (could be
listing online users, could be a URL to share offline, etc.)
-   Once chatting, send messages from one user to the other in a
timely (say, less than a second) manner, in both directions.

#### Bonus functionalities

-   Make timestamps available, and/or shown by default in a
"non-spammy" sort of way.
-   OAuth-based login against one or more existing providers
(Google, twitter, facebook, etc.)
-   Store chat history, allow displaying and/or searching of it.

### Chatbot

Create a "[bot](https://en.wikipedia.org/wiki/Internet_bot)" that will connect to an existing chat service
(e.g. using the [Slack API](https://api.slack.com/)), and interact with messages on that
channel.

#### MVP requirements

-   Connect to an appropriate chat service
-   Respond to "direct messages" / "mentions" in some manner
-   Have some set of "commands" that, if presented after the
mention, will cause the bot to insert certain (possibly
dynamic) responses.

#### Bonus functionalities

-   Have a set of things that the bot will look for in messages
that *do not* mention the bot, to which the bot will respond
anyway.  For example:
-   If it sees the word "weather" in a message that ends with a
question mark, it looks up the current weather and reports
that to the channel.  Double-bonus: if a location is also
mentioned, it looks up weather in that particular place.
-   If it sees an expression of dismay ("this sucks", ":(",
etc.), it responds with an affirmation and/or validation of
some kind.

# Useful resources

I've created some resources for using [Vagrant](https://vagrantup.com/) to help get projects
started more easily.
