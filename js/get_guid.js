function get_A(){
    a = (new Date).getUTCMilliseconds()
    a = String(Math.round(2147483647 * Math.random()) * a % 1e10)
    return a;
}