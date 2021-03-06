The case of the missing values: SQL's coalesce function for Python
==================================================================

date

:   2012-01-17 20:11

author

:   reece

category

:   Computing, Databases, Python

slug

:   471

status

:   draft

Dealing with potentially missing values is annoying, especially when
analyzing sparse data whose structure and completeness is unknown. It's
typically impossible to guess which data might be missing. A set of test
data might be missing different values that those in another data set,
which is to say that you'll succeed on tests and fail in production.
Having a simple way to deal with missing values, especially ones with
easy defaults, is handy.

SQL handles this situation with COALESCE, a function that returns the
first non-NULL value in an array/list of values. IFNULL is a
two-argument version of COALESCE. Conceptually, these are equivalent to
the pseudo-code "if value\_1 is not null then value\_1 else ... if
value\_i-1 is not null return value\_i-1 else return value\_i".

The same circumstances happen in all languages, including Python. For
example, imagine this:

full\_name = first\_name + " " + middle\_name + " " + last\_name

If middle\_name isn't defined, this is an error. In many circumstances,
you don't care about the middle name. What to do?

You could wrap the whole thing in a try...except, and try again with
only first\_name and last\_name.

Or you could check middle\_name
