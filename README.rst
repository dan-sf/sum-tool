README for unix_sum
===================

Command line utility used to sum and format data from stdin. Input data must be sorted on the groupBy column for proper summing.

Usage
-----

.. code-block:: bash

    usage: sum.py [-h] -s SUM_COL [-g GROUPBY] [-f FIELD] [-c CHAR]

    optional arguments:
      -h, --help            show this help message and exit
      -s SUM_COL, --sum_col SUM_COL
                            Comma delim list of columns to sum on, this argument
                            is required, zero based.
      -g GROUPBY, --groupby GROUPBY
                            Comma delim list of columns to group by. If not used,
                            all input will be grouped, zero based.
      -f FIELD, --field FIELD
                            Comma delim list of fields to be printed, zero based.
      -c CHAR, --char CHAR  Input field delimiter, defaults to tab.

Example
-------

.. code-block:: bash

    $ cat file
    201308	data_type_1	13529
    201309	data_type_1	390
    201310	data_type_2	28223
    201312	data_type_2	2239
    201401	data_type_2	89
    201310	data_type_1	14145
    201311	data_type_1	23368
    201312	data_type_1	24183
    201401	data_type_1	29616
    201402	data_type_1	23753
    201308	data_type_2	24474
    201309	data_type_2	9601
    201402	data_type_2	11123
    $ cat file | sort -k2,2 | sum.py -g 1 -s 2 -f 1,2
    data_type_1	128984
    data_type_2	75749

