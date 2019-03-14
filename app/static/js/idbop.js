var dbPromise = idb.open('Tecnico-db', 1, function (upgradeDb) {
    upgradeDb.createObjectStore('Tecnico', { keyPath: 'pk' });
});

fetch('http://127.0.0.1:8000/getdata').then(function (response) {
    return response.json();
}).then(function (jsondata) {
    console.log(jsondata);
});

fetch('http://127.0.0.1:8000/getdata').then(function (response) {
    return response.json();
}).then(function (jsondata) {
    dbPromise.then(function (db) {
        var tx = db.transaction('Tecnico', 'readwrite');
        var feedsStore = tx.objectStore('Tecnico');
        for (var key in jsondata) {
            if (jsondata.hasOwnProperty(key)) {
                feedsStore.put(jsondata[key]);
            }
        }
    });
});

// var post = "";
// dbPromise.then(function (db) {
//     var tx = db.transaction('Tecnico', 'readonly');
//     var feedsStore = tx.objectStore('Tecnico');
//     return feedsStore.openCursor();
// }).then(function logItems(cursor) {
//     if (!cursor) {
//         document.getElementById('offlinedata').innerHTML = post;
//         return;
//     }
//     for (var field in cursor.value) {
//         if (field == 'fields') {
//             feedsData = cursor.value[field];
//             for (var key in feedsData) {
//                 if (key == 'usuario') {
//                     var usuario = '<p>' + feedsData[key] + '</p>';
//                 }
//                 if (key == 'password') {
//                     var password = '<p>' + feedsData[key] + '</p>';
//                 }
//                 if (key == 'es_tecnico') {
//                     var es_tecnico = '<p>' + feedsData[key] + '</p>';
//                 }
//             }
//             // post=post+'<br>'+nombre+'<br>'+estado+'<br>'+comentario+'<br>';
//             post = post + ' ' + usuario + ' ' + password + ' ' + es_tecnico + ' ';

//         }
//     }
//     return cursor.continue().then(logItems);
// });
