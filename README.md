<p>Usage:<br>
&nbsp;&nbsp;TINS.py &lt;options&gt;<br>
<br>
Options:<br>
-h, --help [this info]<br>
-s, --server, --target [target mail server]<br>
-p, --port [target port]<br>
-t, --to, --recipient [recipient]<br>
-f, --from, --sender [sender]<br>
-x, --xm, --x-mailer [X-Mailer header]<br>
–mix, --mixed [use multipart/mixed instead of multipart/alternative]<br>
–to-header [to: header if different from recipient]<br>
–from-header [from: header if different from sender]<br>
–body-text [text body string]<br>
–body-html [html body string]<br>
–text-encode, --text-charset [character encoding for text section]<br>
–html-encode, --html-charset [character encoding for html section]<br>
–encode, --charset [character encoding for both text and html sections (overrides --text-encode/–text-charset/–html-encode/–html-charset)]<br>
–high, --low [message importance (default is medium)]<br>
–ssl, --tls [use ssl/tls]<br>
–url [include malicious url]<br>
–ssn [include ssn numbers]<br>
–av, --virus [include eicar test virus]<br>
–zip [include password protected zip file]<br>
–eml, --write [write email to eml file]<br>
–no-send [do not send email (implies --eml/–write)]<br>
–eml-name [email file name (implies --eml/–write)]<br>
–no-text [no text body]<br>
–no-html [no html body]<br>
–spam [generate test spam]<br>
–adult [generate test adult spam (overrides --spam)]<br>
–dbg, --debug [additional debug information]<br>
–text-body [text body from specified file]<br>
–html-body [html body from specified file]<br>
–attach [attach specified file]</p>