package editor;





import org.fxmisc.richtext.CodeArea;
import org.fxmisc.richtext.LineNumberFactory;
import javafx.scene.control.Label;

import java.awt.*;

import static editor.syntaxe.SyntaxHighlighter.computeHighlighting;
import static java.awt.Color.red;

public class CodeEditor extends CodeArea {


    public CodeEditor() {

        super();

        this.setParagraphGraphicFactory(line -> {
            Label lineNumber = new Label(String.valueOf(line + 1));

            lineNumber.setStyle(
                    "-fx-background-color: #2b2b2b;" +
                            "-fx-text-fill: #d4d4d4;" +
                            "-fx-padding: 0 5 0 5;"
            );

            return lineNumber;
        });




                    //ajout de la coloration
        textProperty().addListener((obs, oldText, newText) -> {
            setStyleSpans(0, computeHighlighting(newText));
        });
        getStylesheets().add(
                getClass().getResource("/code-style.css").toExternalForm()
        );







    }
// Texte -> Matcher (Regex) -> find() -> styleClass -> StyleSpansBuilder -> setStyleSpans() -> CodeArea


}