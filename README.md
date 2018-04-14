# blog
hugo-based blog



# How this was built:

make a repo at github (reece/blog)
hg clone git@github.com:reece/blog.git
(I use hg-git)
cd blog
hugo new site . --force
hg add config.toml




$ mkdir themes
$ cd themes
$ git clone https://github.com/kakawait/hugo-tranquilpeak-theme.git


for f in *.rst; do pandoc -f rst -t markdown $f -o ${f%.rst}.md; git rm $f; done
