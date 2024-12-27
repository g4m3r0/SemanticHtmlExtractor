using Textify;

namespace SemanticHtmlExtractor
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello, World!");

            var html = new HttpClient().GetStringAsync("https://vsr.informatik.tu-chemnitz.de/about/people/").Result;

            HtmlToTextConverter converter = new HtmlToTextConverter();
            string output = converter.Convert(html);

            Console.WriteLine(output);
        }
    }
}