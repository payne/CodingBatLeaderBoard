package org.mattpayne.done;

public class Problem {
    private final String problemName, problemUrl;

    public Problem(String problemName, String problemUrl) {
        this.problemName = problemName;
        this.problemUrl = problemUrl;
    }

    public String toString() {
        return String.format("Problem(%s,%s)", problemName, problemUrl);
    }

}
