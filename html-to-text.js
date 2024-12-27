const axios = require('axios');
const jsdom = require('jsdom');
const { JSDOM } = jsdom;
const textify = require('textify');

axios.get('https://vsr.informatik.tu-chemnitz.de/about/people/')
    .then(response => {
        const dom = new JSDOM(response.data);
        const text = textify(dom.window.document.body, { ignoreLinks: false });
        HtmlToTextConverter converter = new HtmlToTextConverter();
        string output = converter.Convert(html);

        console.log(output);
    })
    .catch(error => {
        console.error(`Failed to fetch page content: ${error}`);
    });
