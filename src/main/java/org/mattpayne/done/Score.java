package org.mattpayne.done;

public class Score implements Comparable {
    String url;
    long solved;

    public Score(String url, long solved) {
        this.url = url;
        this.solved = solved;
    }

    public String toString() {
        return String.format("Score(%s, solved %d", url, solved);
    }

    @Override
    public int compareTo(Object o) {
        Score other = (Score) o;
        return (int) (other.solved - solved);
    }
}
