let port = browser.runtime.connectNative("firefox_launcherentry_integration");
let timeoutHandle = null;

function roundToThree(num) {
    return +(Math.round(num + "e+3") + "e-3");
}

function update() {
    clearTimeout(timeoutHandle);

    let searching = browser.downloads.search({ "state": "in_progress" });
    searching.then((downloadItems) => {
        // make the progressbar the sum of all progresses ?
        let count = downloadItems.length;
        let progress = 0;
        if (count > 0 && downloadItems[0].totalBytes !== -1) {
            progress = roundToThree(downloadItems[0].bytesReceived / downloadItems[0].totalBytes);
        }
        let msg = count + ":" + progress;

        port.postMessage(msg);
        // console.log("sent msg: " + msg);

        // only repeat update if there are active downloads
        if (count > 0) {
            timeoutHandle = setTimeout(update, 1000);
        }
    })
}

browser.downloads.onCreated.addListener(update);
browser.downloads.onChanged.addListener(update);
