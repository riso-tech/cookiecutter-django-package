# Cookiecutter Django Package

Powered by [Cookiecutter](https://github.com/cookiecutter/cookiecutter), Cookiecutter Django is a framework for generate new Django Package quickly.

## Usage

Let's pretend you want to create a Django project called "redditclone". Rather than using `startproject`
and then editing the results to include your name, email, and various configuration issues that always get forgotten until the worst possible moment, get [cookiecutter](https://github.com/cookiecutter/cookiecutter) to do all the work.

First, get Cookiecutter. Trust me, it's awesome:

    $ pip install "cookiecutter>=1.7.0"

Now run it against this repo:

    $ cookiecutter https://github.com/riso-tech/cookiecutter-django-package

You'll be prompted for some values. Provide them, then a Django Package project will be created for you.

**Warning**: After this point, change 'Bin Nguyen', 'riso-tech', etc to your own information.

Answer the prompts with your own desired [options](http://cookiecutter-django.readthedocs.io/en/latest/project-generation-options.html). For example:

    Cloning into 'cookiecutter-django-admin'...
    remote: Counting objects: 550, done.
    remote: Compressing objects: 100% (310/310), done.
    remote: Total 550 (delta 283), reused 479 (delta 222)
    Receiving objects: 100% (550/550), 127.66 KiB | 58 KiB/s, done.
    Resolving deltas: 100% (283/283), done.
    project_name [My Awesome Package]: Reddit Clone
    project_slug [reddit_clone]: reddit
    app_slug [reddit_clone]: reddit
    description [Behold My Awesome Package!]: A reddit clone.
    author_name [Bin Nguyen]: Bin Nguyen
    repo_url [https://github.com/riso-tech/reddit]

Enter the project and take a look around:

    $ cd reddit/
    $ ls

Create a git repo and push it there:

    $ git init
    $ git add .
    $ git commit -m "first awesome commit"
    $ git remote add origin git@github.com:riso-tech/redditclone.git
    $ git push -u origin master

Now take a look at your repo. Don't forget to carefully look at the generated README. Awesome, right?

## Not Exactly What You Want?

This is what I want. *It might not be what you want.* Don't worry, you have options:

### Fork This

If you have differences in your preferred setup, I encourage you to fork this to create your own version.
Once you have your fork working, let me know and I'll add it to a '*Similar Cookiecutter Templates*' list here.
It's up to you whether to rename your fork.

If you do rename your fork, I encourage you to submit it to the following places:

-   [cookiecutter](https://github.com/cookiecutter/cookiecutter) so it gets listed in the README as a template.
-   The cookiecutter [grid](https://www.djangopackages.com/grids/g/cookiecutters/) on Django Packages.

### Submit a Pull Request

We accept pull requests if they're small, atomic, and make our own project development
experience better.
