public class metadata_classifier {
    public static void main(String[] args) {
        JDBC myDB = new JDBC();
        myDB.connect("select Is_metadata from corpus where ID=26780095");


    }

}