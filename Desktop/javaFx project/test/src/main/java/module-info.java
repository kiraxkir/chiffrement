module  org.example {
    requires javafx.controls;
    requires javafx.fxml;
    requires org.fxmisc.richtext;
    requires java.desktop;
    requires org.fxmisc.flowless;
    requires jdk.jfr;
    requires com.fasterxml.jackson.databind;
    requires java.sql;

    opens org.example to javafx.fxml;
    opens editor to com.fasterxml.jackson.databind;

    exports org.example;
}
