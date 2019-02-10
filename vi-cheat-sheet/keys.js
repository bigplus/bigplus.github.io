function setmode(classname) {
	// set style for each #rows>li>ul>li to display:none unless it matches classname
	var showclass = classname ? '^mode '+classname+'(?!\\w)' : '^(?!mode)';
	var rows = document.getElementById('rows').getElementsByTagName('TR');
	for (var i = 0; i < rows.length; i++) {
		var el = rows[i];
		el.style.display = el.className.match(showclass) ? 'block' : 'none';
	}

	// update H2 to reflect the first part of a currently active (but hidden) row header
	var h3s = document.getElementsByTagName('TH');
	for (var i = 0; i < h3s.length; i++) {
		if (h3s[i].parentNode.style.display != 'block') continue;
		document.getElementsByTagName('H2')[0].innerHTML = h3s[i].firstChild.data;
	}
}

var keyfocus = undefined;
document.onkeypress = function(e) {
	var keylabels = document.getElementById('rows').getElementsByTagName('B');
	var keys = {};
	for (var i = 0; i < keylabels.length; i++) {
		keys[keylabels[i].innerHTML] = keylabels[i].parentNode;
	}
	var input = e.charCode || e.keyCode;
	for (var i = 0; i < keylabels.length; i++) {
		var key = keylabels[i].parentNode;
		if (!key.onclick) continue;
		var keychar = key.className.match(/ chr(\d+)$/);
		if (!keychar) continue; // not enterable
		keychar = keychar[1];
		if (keychar != input) continue; // different key
		var row = key.parentNode;
		var keymod = row.className;
		if ((keymod.search(/\bctrl\b/) != -1) != e.ctrlKey) continue; // modifier mismatch
		if ((keymod.search(/\bmeta\b/) != -1) != e.altKey) continue;
		var shown = row.style.display != 'none';
		if (!shown) continue; // foreign mode
		if (keyfocus) keyfocus.style.outline = '';
		key.style.outline = '1px solid red';
		keyfocus = key;
		if (key.onclick) key.onclick();
		return false;
	}
}
