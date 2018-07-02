package org.mattpayne.done.parser;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

import java.io.IOException;

public class CodingBatDone {
    public static void main(String[] args) throws IOException {
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
