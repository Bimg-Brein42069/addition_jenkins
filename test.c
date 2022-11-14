#include <assert.h>
#include "add.h"

int main(){
    assert(add(0,0) == 0);
    assert(add(1,2) == 3);
    assert(add(-1,2) == 1);
    assert(add(2000000000,2000000000) == 4000000000);
    assert(add(-2000000000,-2000000000) == -4000000000);
    return 0;
}
