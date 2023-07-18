var a = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
const decode = function(e) {
    for (var t, n, r, i, o, c, s = "", l = 0, u = e.replace(/[^A-Za-z0-9+/=]/g, ""); l < e.length; )
        t = a.indexOf(u.charAt(l++)) << 2 | (i = a.indexOf(u.charAt(l++))) >> 4,
        n = (15 & i) << 4 | (o = a.indexOf(u.charAt(l++))) >> 2,
        r = (3 & o) << 6 | (c = a.indexOf(u.charAt(l++))),
        mm = String.fromCharCode(t),
        s += String.fromCharCode(t),
        64 !== o && (s += String.fromCharCode(n)),
        64 !== c && (s += String.fromCharCode(r));
    return s = function(e) {
        for (var t = "", n = 0, a = 0, r = 0, i = 0; n < e.length; )
            (a = e.charCodeAt(n)) < 128 ? (t += String.fromCharCode(a),
            n++) : a > 191 && a < 224 ? (r = e.charCodeAt(n + 1),
            t += String.fromCharCode((31 & a) << 6 | 63 & r),
            n += 2) : (r = e.charCodeAt(n + 1),
            i = e.charCodeAt(n + 2),
            t += String.fromCharCode((15 & a) << 12 | (63 & r) << 6 | 63 & i),
            n += 3);
        return t
    }(s)
}

function get_lyric(lyric){
    return decode(lyric)
}