SELECT vname, name, isbn FROM t_leser, t_verleih;

SELECT vname, name, isbn FROM t_leser, t_verleih ORDER BY vname, name;

SELECT vname, name, isbn FROM t_leser JOIN t_verleih WHERE nr=leser;

SELECT vname, name, isbn FROM t_leser JOIN t_verleih JOIN WHERE nr=leser;