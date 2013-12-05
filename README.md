GitHub Flavored Markdown
================================

*View the [source of this content](http://github.github.com/github-flavored-markdown/sample_content.html).*

Let's get the whole "linebreak" thing out of the way. The next paragraph contains two phrases separated by a single newline character:

Roses are red
Violets are blue

The next paragraph has the same phrases, but now they are separated by two spaces and a newline character:

Roses are red  
Violets are blue

Oh, and one thing I cannot stand is the mangling of words with multiple underscores in them like perform_complicated_task or do_this_and_do_that_and_another_thing.

A bit of the GitHub spice
-------------------------

In addition to the changes in the previous section, certain references are auto-linked:

* SHA: be6a8cc1c1ecfe9489fb51e4869af15a13fc2cd2
* User@SHA ref: mojombo@be6a8cc1c1ecfe9489fb51e4869af15a13fc2cd2
* User/Project@SHA: mojombo/god@be6a8cc1c1ecfe9489fb51e4869af15a13fc2cd2
* \#Num: #1
* User/#Num: mojombo#1
* User/Project#Num: mojombo/god#1

These are dangerous goodies though, and we need to make sure email addresses don't get mangled:

My email addy is tom@github.com.

Math is hard, let's go shopping
-------------------------------

In first grade I learned that 5 > 3 and 2 < 7. Maybe some arrows. 1 -> 2 -> 3. 9 <- 8 <- 7.

Triangles man! a^2 + b^2 = c^2

We all like making lists
------------------------

The above header should be an H2 tag. Now, for a list of fruits:

* Red Apples
* Purple Grapes
* Green Kiwifruits

Let's get crazy:

1.  This is a list item with two paragraphs. Lorem ipsum dolor
    sit amet, consectetuer adipiscing elit. Aliquam hendrerit
    mi posuere lectus.

    Vestibulum enim wisi, viverra nec, fringilla in, laoreet
    vitae, risus. Donec sit amet nisl. Aliquam semper ipsum
    sit amet velit.

2.  Suspendisse id sem consectetuer libero luctus adipiscing.

What about some code **in** a list? That's insane, right?

1. In Ruby you can map like this:

        ['a', 'b'].map { |x| x.uppercase }

2. In Rails, you can do a shortcut:

        ['a', 'b'].map(&:uppercase)

Some people seem to like definition lists

<dl>
  <dt>Lower cost</dt>
  <dd>The new version of this product costs significantly less than the previous one!</dd>
  <dt>Easier to use</dt>
  <dd>We've changed the product so that it's much easier to use!</dd>
</dl>

I am a robot
------------

Maybe you want to print `robot` to the console 1000 times. Why not?

    def robot_invasion
      puts("robot " * 1000)
    end

You see, that was formatted as code because it's been indented by four spaces.

How about we throw some angle braces and ampersands in there?

    <div class="footer">
        &copy; 2004 Foo Corporation
    </div>

Set in stone
------------

Preformatted blocks are useful for ASCII art:

<pre>
             ,-. 
    ,     ,-.   ,-. 
   / \   (   )-(   ) 
   \ |  ,.>-(   )-< 
    \|,' (   )-(   ) 
     Y ___`-'   `-' 
     |/__/   `-' 
     | 
     | 
     |    -hrr- 
  ___|_____________ 
</pre>

Playing the blame game
----------------------

If you need to blame someone, the best way to do so is by quoting them:

> I, at any rate, am convinced that He does not throw dice.

Or perhaps someone a little less eloquent:

> I wish you'd have given me this written question ahead of time so I
> could plan for it... I'm sure something will pop into my head here in
> the midst of this press conference, with all the pressure of trying to
> come up with answer, but it hadn't yet...
>
> I don't want to sound like
> I have made no mistakes. I'm confident I have. I just haven't - you
> just put me under the spot here, and maybe I'm not as quick on my feet
> as I should be in coming up with one.

Table for two
-------------

<table>
  <tr>
    <th>ID</th><th>Name</th><th>Rank</th>
  </tr>
  <tr>
    <td>1</td><td>Tom Preston-Werner</td><td>Awesome</td>
  </tr>
  <tr>
    <td>2</td><td>Albert Einstein</td><td>Nearly as awesome</td>
  </tr>
</table>

Crazy linking action
--------------------

I get 10 times more traffic from [Google] [1] than from
[Yahoo] [2] or [MSN] [3].

  [1]: http://google.com/        "Google"
  [2]: http://search.yahoo.com/  "Yahoo Search"
  [3]: http://search.msn.com/    "MSN Search"











An application for crowdsourcing food sources in food sheds.

For now we are using the [Fork & Pull Model of development](https://help.github.com/articles/using-pull-requests)

1.) Fork the [main repo](https://github.com/food-mappers/food-mapper-app)

After the repo is forked and created at 'your-github-username/food-mapper-app', clone your repo

	git clone https://github.com/your-github-username/food-mapper-app.git

or

	git clone git@github.com:your-github-username/food-mapper-app.git

2.) Create new virtual environement

	cd food-mapper-app
	virtualenv env
	source env/bin/activate
	pip install -r requirements.txt

3a.) Create the database and users

	createdb food_map_test
	psql -d food_map_test
	CREATE USER foodmapper WITH PASSWORD 'foodmapper';
	GRANT ALL PRIVILEGES ON food_map_test to foodmapper;
	\q

3a.1) You might have trouble with PostGRES when trying to run the app.

	To complete the syncdb command, I needed to hack around adding links to the libraries needed by postgres.

	First make a directory, then make some symlinks to missing libs.


	> mkdir food-mapper-app/env/lib/python2.7/site-packages/lib
	> ln -s /Applications/Postgres.app/Contents/MacOS/lib/libssl.1.0.0.dylib food-mapper-app/env/lib/python2.7/site-packages/lib/libssl.1.0.0.dylib
	> ln -s /Applications/Postgres.app/Contents/MacOS/lib/libcrypto.1.0.0.dylib food-mapper-app/env/lib/python2.7/site-packages/lib/libcrypto.1.0.0.dylib 


3b.) Run sync db

	python manage.py syncdb
	#seed initial data
	python manage.py loaddata fixtures/map_data
	#load a map with a lot of points
	python manage.py loaddata fixtures/lotsofdata

During syncdb create superuser

4.) Start server

	python manage.py runserver

5.) Navigate to root [http://127.0.0.1:8000](http://127.0.0.1:8000) - Should see map for now

6.) Signin with user you created - now you can create a community

7.) Navigate to root/communities, create a community

8.) Navigate to root/sources, create a food source.
