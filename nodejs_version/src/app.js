const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');
const axios = require('axios');
const cheerio = require('cheerio');
const archiver = require('archiver');
const { Readable } = require('stream');

const app = express();
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, '../public')));

app.post('/', async (req, res) => {
    try {
        const url = req.body.url;
        const links = await extractImageLinksFromUrl(url);

        const zipStream = await createZipStream(links);
        res.setHeader('Content-Disposition', 'attachment; filename=images.zip');
        zipStream.pipe(res);
    } catch (error) {
        res.status(500).send('Error occurred: ' + error.message);
    }
});

async function extractImageLinksFromUrl(url) {
    const response = await axios.get(url);
    const $ = cheerio.load(response.data);
    const parentDiv = $('div.image-list');
    const imgTags = parentDiv.find('img').toArray();

    const allowedExtensions = ['.jpeg', '.jpg', '.png', '.gif', '.bmp'];
    const srcLinks = imgTags.map(img => $(img).attr('src'))
        .filter(src => allowedExtensions.some(ext => src.includes(ext)) && !src.toLowerCase().includes('video'))
        .map(src => src.slice(0, -12));
    return srcLinks;
}

async function createZipStream(links) {
    const archive = archiver('zip', { zlib: { level: 9 } });
    const stream = new Readable().wrap(archive);

    for (let i = 0; i < links.length; i++) {
        const link = links[i];
        const response = await axios.get(link, { responseType: 'arraybuffer' });
        const fileExt = link.split('.').pop();
        archive.append(response.data, { name: `image_${i + 1}.${fileExt}` });
    }

    archive.finalize();
    return stream;
}

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
