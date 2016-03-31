# Conventions

- Read and pay attention to current code in the repository
- For the Python part, we follow pep8 in most cases. We use [flake8][flake8] to check for linting errors. Once you're ready to commit changes, check your code with `flake8`.
- Install a plugin for [EditorConfig][editorconfig] and let it handle some of the formating issues for you.
- For the Django part, we follow standard [Django coding style][django-coding-style].
- For contributing, we use [git flow][git-flow] which automate the branching workflow


# Coding Rules

### Django models

- All model names in singular and CamelCase.
- All models have a `Meta` with at least:
    * `verbose_name` and `verbose_name_plural`: unicode strings, lowercase, with spaces.
    * `ordering`: return a consistent order, using pk if no other unique field or combination exists.
- All fields have `verbose_name`. Also `help_text` if needed to fully explain the field meaning.
- All fields have explicit `blank` and `null` parameters. Use only those combinations, unless there a documented need of other thing:

    **Normal fields** (IntegerField, DateField, ForeignKey, FileField...)
      * (optional) `null = True`, `blank = True`
      * (required) `null = False`, `blank = False`

    **Text fields** (CharField, TextField, URLField...)
      * (optional) `null = False`, `blank = True`
      * (required) `null = False`, `blank = False`

    **Boolean fields**:
      * (two values, T/F) `null = False`, `blank = True`
      * (three values, T/F/Null) `null = True`, `blank = True`

- Don't create text fields with `null = True`, unless you need to distinguish between empty string and `None`.
- Don't create boolean fields with `blank = False`, otherwise they could only be `True`.

Example:

```python
class SomeClass(models.Model):
    name = models.CharField(max_length=100, null = False, blank = False, unique=True,
               verbose_name = _(u'name'))
    slug = models.SlugField(max_length=100, null = False, blank = False, unique=True,
               verbose_name = _(u'slug'),
               help_text = (u'Identifier of this object. Only letters, digits and underscore "_" allowed.'))
    text = models.TextField(null = False, blank = True,
               verbose_name = _(u'text'))

    class Meta:
        verbose_name = _(u'some class')
        verbose_name_plural = _(u'some classes')
        ordering = ['name']

    def __unicode__(self):
        return self.name
```

# Setup

Minimum requirements: **python3, pip & postgres**.
We advise to use [`virtualenv`][virtualenv] with python3 interprator.

* Look at [postgres installation instruction][install-postgres]

## Getting up and running

```
pip install -r requirements.txt
createdb askcoding
python manage.py migrate
```

# Git Flow

We follow `git-flow` for development/release. To learn more about git-flow look at this [link][gitflow-model]

## Installing git-flow

Look at these up-to-date [installation Instructions][install-git-flow]

## Setting up git-flow

After installing git-flow, you can start using git-flow in your repository by using it's init command. Select all the default options as:

```bash
$ git flow init

Which branch should be used for bringing forth production releases?
   - develop
   - master
   - update-readme
Branch name for production releases: [master]

Which branch should be used for integration of the "next release"?
   - develop
   - update-readme
Branch name for "next release" development: [develop]

How to name your supporting branch prefixes?
Feature branches? [feature/]
Release branches? [release/]
Hotfix branches? [hotfix/]
Support branches? [support/]
Version tag prefix? []
```

__NOTE__: All the new branches are feature branches except hotfix and must be derived from `develop` branch. Instead of `release` branches `master` branch acts as current stable release.

To create or start a new feature branch with the name of new feature (in this case, "authentication"):

```bash
$ git flow feature start authentication develop
Switched to a new branch 'feature/authentication'

Summary of actions:
- A new branch 'feature/authentication' was created, based on 'develop'
- You are now on branch 'feature/authentication'

Now, start committing on your feature. When done, use:

    git flow feature finish update-readme
```

As the output already explains, you're now on a new branch you can use to work on your feature. Use git like you normally would, and push your changes using `feature publish` when changes committed. To finish the feature when it's done use `feature finish`. `feature finish` command merge the feature to develop branch and delete the feature branch. So, before finish get your pull request approved:

```bash
$ git flow feature publish authentication
Counting objects: 4, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 1.85 KiB | 0 bytes/s, done.
Total 4 (delta 2), reused 0 (delta 0)
To git@github.com:akarambir/askcoding.git
 * [new branch]      feature/update-readme -> feature/update-readme
Already on 'feature/authentication'
Your branch is up-to-date with 'origin/feature/authentication'.

Summary of actions:
- A new remote branch 'feature/authentication' was created
- The local branch 'feature/authentication' was configured to track the remote branch
- You are now on branch 'feature/authentication'
```
```bash
$ git flow feature finish authentication
Switched to branch 'develop'
Updating 9060376..00bafe4
Fast-forward
 authentication.txt | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 authentication.txt
Deleted branch feature/authentication (was 00bafe4).

Summary of actions:
- The feature branch 'feature/authentication' was merged into 'develop'
- Feature branch 'feature/authentication' has been removed
- You are now on branch 'develop'
```

Git-flow is a wrapper around git commands. To check the corresponding raw `git` commands for a `git-flow` command have a look at this [link][gitflow-breakdown].

# Useful Commands

Run these commands before pushing the code:

* Testing
```
py.test --cov -v --pdb
```

* Linting
```
flake8 .
```

__NOTE__: We try to keep code coverage more than 90%. If it is dropping below 90% than its a concern. Check [coveralls] for this.

[editorconfig]: http://editorconfig.org/
[flake8]: http://flake8.readthedocs.org/en/latest/
[django-coding-style]: https://docs.djangoproject.com/en/1.7/internals/contributin/writing-code/coding-style/
[git-flow]: https://github.com/nvie/gitflow

[install-postgres]: https://wiki.postgresql.org/wiki/Detailed_installation_guide
[virtualenv]: https://virtualenv.pypa.io/en/latest/

[gitflow-breakdown]: https://gist.github.com/JamesMGreene/cdd0ac49f90c987e45ac
[gitflow-model]: http://nvie.com/posts/a-successful-git-branching-model/
[install-git-flow]: https://github.com/nvie/gitflow/wiki/Installation
[coveralls]: https://coveralls.io/github/akarambir/askcoding?branch=master
