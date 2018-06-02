create table enemies_flash as 
    Select "thawne" as name, "true" as speedster, 9 as rating, 10 as intelligence union
    Select "zoom"          , "true"             ,8          ,7 union
    Select "savitar"       , "true"              ,7          ,3 union
    Select "devoe", "false",8,20 union
    Select "Captain cold" , "false", 6,8 union
    Select "abra-cadabra", "false", 3, 5 union
    Select "Gorrila Grodd", "false",2,10 order by intelligence;


create table "team flash" as

Select "Flash" as name, "Super-speed" as power, 10 as status union
Select "Killer Frost", "Freezing",10 union
Select "Vibe", "Dimensional telekinesis", 8 union
Select "Arrow", "Skillful at Arrow", 9 union
Select "Harrison Wells","Genius",9 union
Select "Wally West", "Super-speed",7 union
Select "Jay garrick", "Super-speed",5 union
Select "Ralph Dibny", "Elasticity", 9;

create table if not exists Human(name unique ,relationship Default "friend",rating);

