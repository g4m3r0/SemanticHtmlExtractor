namespace SemanticHtmlExtractor.WinForms;

using Textify;

public partial class Form1 : Form
{
    public Form1()
    {
        InitializeComponent();
    }

    private void button1_Click(object sender, EventArgs e)
    {
        var html = new HttpClient().GetStringAsync(textBox1.Text).Result;

        HtmlToTextConverter converter = new HtmlToTextConverter();
        string output = converter.Convert(html);

        richTextBox1.Text = output;
    }
}