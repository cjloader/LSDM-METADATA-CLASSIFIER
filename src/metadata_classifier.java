public class metadata_classifier {
    public static void main(String[] args) {
        JDBC myDB = new JDBC();
        myDB.connect("select * from corpus where Is_metadata=1");

        myDB.connect("select count(*) from corpus");

    }

}