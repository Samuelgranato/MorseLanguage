OPENPROGRAM
OPENBLOCK
    function independence(@x) OPENBLOCK
        @x = 42:
        return @x:
        CLOSEBLOCK
    @x = 10 MULT 2:
    independence(@x):
    echo @x:
    echo "a" CONCAT "b":

    @x1 = 3:
    @x1 = @x1 +1:

    echo @x1:

    @y1 = @x1 MULT 100:
    echo @y1:

    if (1 == 1) OPENBLOCK
        echo "TRUEEEE":
    CLOSEBLOCK else OPENBLOCK
        echo 0:
    CLOSEBLOCK

    if (1 LESS 0) OPENBLOCK
        echo "0":
    CLOSEBLOCK else OPENBLOCK
        echo "FALSEEEEEEEEEEEEE":
    CLOSEBLOCK


    @a3333 = 5:

    while(@a3333 GREATER 0) OPENBLOCK
        echo @a3333:
        @a3333 = @a3333 - 1:
    CLOSEBLOCK


    function teste() OPENBLOCK
        echo "FUNCTION":
    CLOSEBLOCK

    teste():

    echo 2 MULT 2 MULT 10 / 2 + 500:


CLOSEBLOCK
CLOSEPROGRAM