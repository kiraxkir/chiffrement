package editor.syntaxe;


import org.fxmisc.richtext.model.StyleSpans;
import org.fxmisc.richtext.model.StyleSpansBuilder;

import java.util.Collection;
import java.util.Collections;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class SyntaxHighlighter {

    // regex java
    private static final String[] KEYWORDS = new String[] {
            "abstract", "assert", "boolean", "break", "byte",
            "case", "catch", "char", "class", "const",
            "continue", "default", "do", "double", "else",
            "enum", "extends", "final", "finally", "float",
            "for", "goto", "if", "implements", "import",
            "instanceof", "int", "interface", "long", "native",
            "new", "package", "private", "protected", "public",
            "return", "short", "static", "strictfp", "super",
            "switch", "synchronized", "this", "throw", "throws",
            "transient", "try", "void", "volatile", "while","main","IO","String"

    };
    private static final String[] OUTPUT = new String[]{
            "print", " System.out.println() ","scanner","range",
    };


    private static final String OUTPUTWORD =
            "\\b(" + String.join("|", OUTPUT) + ")\\b";



    private static final String KEYWORD_PATTERN =
            "\\b(" + String.join("|", KEYWORDS) + ")\\b";

    private static final String PAREN_PATTERN = "\\(|\\)";

    private static final String BRACE_PATTERN = "\\{:|\\}";
    private static final String BRACKET_PATTERN = "\\[|\\]";
    private static final String SEMICOLON_PATTERN = "\\;";
    private static final String STRING_PATTERN = "\"([^\"\\\\]|\\\\.)*\"";
    // regex pour les commentaire  premier partie c est tout les les mot qui commence par // sauf les saut de ligne
    private static final String COMMENT_PATTERN = "//[^\n]*" + "|" + "/\\*(.|\\R)*?\\*/";


    //la c est pour creer le groupe
    private static final Pattern PATTERN = Pattern.compile(
            "(?<KEYWORD>" + KEYWORD_PATTERN + ")"
                    + "|(?<OUT>" + OUTPUTWORD + ")"       // <- nouveau groupe pour outputs
                    + "|(?<COMMENT>" + COMMENT_PATTERN + ")"
                    + "|(?<STRING>" + STRING_PATTERN + ")"
                    + "|(?<PAREN>" + PAREN_PATTERN + ")"
                    + "|(?<BRACE>" + BRACE_PATTERN + ")"
                    + "|(?<BRACKET>" + BRACKET_PATTERN + ")"
                    + "|(?<SEMICOLON>" + SEMICOLON_PATTERN + ")"
    );

    public static StyleSpans<Collection<String>> computeHighlighting(String text) {
        Matcher matcher = PATTERN.matcher(text);
        int lastKwEnd = 0;

        StyleSpansBuilder<Collection<String>> spansBuilder = new StyleSpansBuilder<>();

        while (matcher.find()) {
            String styleClass =
                    matcher.group("KEYWORD") != null ? "keyword" :
                            matcher.group("OUT") != null ? "sortie" :      // <- ici
                                    matcher.group("PAREN") != null ? "paren" :
                                            matcher.group("BRACE") != null ? "brace" :
                                                    matcher.group("BRACKET") != null ? "bracket" :
                                                            matcher.group("SEMICOLON") != null ? "semicolon" :
                                                                    matcher.group("STRING") != null ? "string" :
                                                                            matcher.group("COMMENT") != null ? "comment" :
                                                                                    "plain";  // style par défaut

            // texte avant le match → style par défaut "plain"
            spansBuilder.add(Collections.singleton("plain"), matcher.start() - lastKwEnd);

            // texte stylisé
            spansBuilder.add(Collections.singleton(styleClass), matcher.end() - matcher.start());

            lastKwEnd = matcher.end();
        }

        // reste du texte après le dernier match → style par défaut
        spansBuilder.add(Collections.singleton("plain"), text.length() - lastKwEnd);

        return spansBuilder.create();
    }

}
