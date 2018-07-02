package org.mattpayne.done;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

import java.io.IOException;

public class ScoreBoard {
    private String fileName;

    public static void main(String[] args) throws IOException {
        try {
            ScoreBoard sb = new ScoreBoard(args);
            sb.run();
            System.out.println("Normal Termination.");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public ScoreBoard(String[] args) {
        this.fileName=args.length > 0 ? args[0] : "secret_people.txt";
    }

    public void run() throws IOException {
        Document doc = Jsoup.connect("http://codingbat.com/done?user=payne@mattpayne.org&tag=6764324312").get();
        log(doc.title());

        Elements newsHeadlines = doc.select("a");
        for (Element headline : newsHeadlines) {
            log("%s\t%s", headline.text(), headline.absUrl("href"));
        }
    }

    private static void log(String msg, String... vals) {
        System.out.println(String.format(msg, vals));
    }
}
