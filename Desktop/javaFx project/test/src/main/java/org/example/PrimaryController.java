package org.example;


import com.fasterxml.jackson.databind.ObjectMapper;

import database.UserDB;
import editor.CodeEditor;
import editor.Question;
import editor.TestCase;

import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextArea;
import javafx.scene.input.MouseEvent;
import javafx.scene.layout.BorderPane;
import org.fxmisc.flowless.VirtualizedScrollPane;
import org.fxmisc.richtext.CodeArea;


import java.io.*;
import java.net.URL;
import java.sql.SQLException;
import java.util.ResourceBundle;

public class PrimaryController implements Initializable {

    @FXML
    private Button btnRun;
    @FXML
    private Button btnchoix;



    @FXML
    private BorderPane pane;





    @FXML
    private Label resultat;

    @FXML
    private TextArea textarea;
    CodeEditor editor;
    private UserDB user = new UserDB();

    @FXML
    void choix(MouseEvent event) throws IOException, SQLException {
        InputStream is = getClass().getResourceAsStream("/questions/q1.json");
        ObjectMapper mapper = new ObjectMapper();

        Question q = mapper.readValue(is, Question.class);

        editor.replaceText(q.template);
        textarea.setText(q.description);





    }
    @FXML
    void run(MouseEvent event) throws IOException, InterruptedException {
        String code = editor.getText();

        // ecrire
        FileWriter writer1 = new FileWriter("code/Main.py");
        writer1.write(code);
        writer1.close();

//        ProcessBuilder builder = new ProcessBuilder("python", "code/Main.py");
//        Process proccess = builder.start();
        InputStream is = getClass().getResourceAsStream("/questions/q1.json");
        ObjectMapper mapper = new ObjectMapper();

        Question q = mapper.readValue(is, Question.class);

        for(TestCase t : q.tests){

            ProcessBuilder builder = new ProcessBuilder("python", "code/Main.py");
            Process process = builder.start();

            BufferedWriter writer =
                    new BufferedWriter(
                            new OutputStreamWriter(process.getOutputStream()));

            writer.write(t.input);
            writer.newLine();
            writer.flush();
            writer.close();

            BufferedReader output =
                    new BufferedReader(
                            new InputStreamReader(process.getInputStream()));

            String line = output.readLine();

            if(line != null && line.equals(t.output)){
                System.out.println("Bonne réponse");
            }else{
                System.out.println("Mauvaise réponse");
            }

            process.waitFor();
        }



    }

    @Override
    public void initialize(URL url, ResourceBundle resourceBundle) {

        editor = new CodeEditor();

        VirtualizedScrollPane<CodeArea> scrollPane =
                new VirtualizedScrollPane<>(editor);

        pane.setCenter(scrollPane);
    }
}