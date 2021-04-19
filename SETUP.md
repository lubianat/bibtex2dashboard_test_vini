
## Manual configuration


First, you must configure two environment variables (`OWNER` and `REPO`).
These variables specify the GitHub repository for the manuscript (i.e. `https://github.com/OWNER/REPO`).
Make sure that the case of `OWNER` matches how your username is displayed on GitHub.
In general, assume that all commands in this setup are case-sensitive.
**Edit the following commands with your manuscript's information:**

```sh
# GitHub username or organization name (change from lubianat)
OWNER=lubianat
# Repository name (change from bibtex2dashboard)
REPO=bibtex2dashboard
```
## Create repository

**Execute the remaining commands verbatim.**
They do not need to be edited (if the setup works as intended).

Next you must clone `lubianat/bibtex2dashboard` and reconfigure the remote repositories:

```sh
# Clone lubianat/bibtex2dashboard
git clone --single-branch https://github.com/lubianat/bibtex2dashboard.git $REPO
cd $REPO

# Configure remotes
git remote add rootstock https://github.com/lubianat/bibtex2dashboard.git

# Option A: Set origin URL using its web address
git remote set-url origin https://github.com/$OWNER/$REPO.git
# Option B: If GitHub SSH key access is enabled for OWNER, run the following command instead
git remote set-url origin git@github.com:$OWNER/$REPO.git
```

Then create an empty repository on GitHub. 
You can do this at <https://github.com/new> or via the [GitHub command line interface](https://github.com/cli/cli) (if installed) with `gh repo create`.

```sh
gh repo create
git branch -m master main
```

Make sure to use the same "Owner" and "Repository name" specified above.
Do not initialize the repository, other than optionally adding a Description.
Next, push your cloned demonstration database:

```sh
git push --set-upstream origin main
```
** README and Database updates

Update `README.md`  and `wbib.py` files to reference your new repository:

```shell
# Perform substitutions
sed "s/lubianat\/bibtex2dashboard/$OWNER\/$REPO/g" README.md > tmp && mv -f tmp README.md
sed "s/lubianat\.github\.io\/bibtex2dashboard/$OWNER\.github\.io\/$REPO/g" README.md > tmp && mv -f tmp README.md
sed "s/lubianat\/bibtex2dashboard/$OWNER\/$REPO/g" wbib/wbib.py > tmp && mv -f tmp wbib/wbib.py
sed "s/lubianat/$OWNER/g" README.md > tmp && mv -f tmp README.md
```

- Add your.bib file with less than 500 articles (more than that and it might break) to the repository 
- Set GitHub Pages on the repository settings on GitHub to the `main` branch 
- Customize `render_dashboard.py` with your title of your web page.
- Run `python3 render_dashboard.py yourbibfile.bib`
- Commit and push everything to GitHub (or just check the newly generated index.html file)

## Acknowledgements

SETUP inspired by [Manubot's rootstock](https://github.com/manubot/rootstock/edit/main/SETUP.md). 
Bits of the SETUP were directly copied from Manubot's SETUP.md (which is released under CC-BY)