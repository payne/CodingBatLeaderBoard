package org.mattpayne.done;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

import java.io.FileReader;
import java.io.IOException;
import java.io.LineNumberReader;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

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
        Map<String, List<Problem>> personUrlToProblems=new HashMap<>();
        LineNumberReader in = new LineNumberReader(new FileReader(this.fileName));
        String line;
        while ((line=in.readLine()) != null) {
            List<Problem> lstProblems = getProblems(line);
            personUrlToProblems.put(line,lstProblems);
        }
        in.close();
        PrintWriter out = new PrintWriter("ScoreBoard.output.txt");
        dump(out, personUrlToProblems);
        out.close();
    }

    private void dump(PrintWriter out, Map<String, List<Problem>> personUrlToProblems) {
        for (String url : personUrlToProblems.keySet()) {
            List<Problem> problems = personUrlToProblems.get(url);
            long pythonCount =
            problems.stream().filter(p -> p.problemName.contains("python")).count();
            long javaCount = problems.size() - pythonCount;
            out.format("%s solved %d java problems and %d python problems\n", url, javaCount, pythonCount);
            int number=1;
            for (Problem problem : problems) {
                out.format("%d\t%s\n", number++, problem);
            }
        }
    }

    private List<Problem> getProblems(String urlStr) throws IOException {
        Document doc = Jsoup.connect(urlStr).get();
        List<Problem> problemList = new ArrayList<>();

        Elements newsHeadlines = doc.select("a");
        for (Element headline : newsHeadlines) {
            String problemName= headline.parent().text();
            String problemUrl = headline.absUrl("href");
            if (problemUrl.contains("prob")) {
                Problem problem = new Problem(problemName, problemUrl);
                problemList.add(problem);
            }
        }
        return problemList;
    }
}
