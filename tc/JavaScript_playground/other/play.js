function addWithSurcharge (a, b) { 
    let surcharge = 0;
    if (a <= 10) {
    let surcharge = 1;
    return a = a + surcharge;
    };
    else if (a > 10 && a <= 20) {
    let surcharge = 2;
    return a = a + surcharge;
    }
    else if (a > 20) {
    let surcharge = 3;
    return a = a + surcharge;
    };
    
    
    if (b <= 10) {
    let surcharge = 1;
    return b = b + surcharge;
    };
    else if (b > 10 && b <= 20) {
    let surcharge = 2;
    return b = b + surcharge;
    };
    else if (b > 20) {
    let surcharge = 3;
    return b = b + surcharge;
    };
    }; 