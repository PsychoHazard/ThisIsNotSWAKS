<p>Usage:<br>
&nbsp;&nbsp;&nbsp;TINS.py &lt;options&gt;<br>
<br>
Options:<br>
&nbsp;&nbsp;&nbsp;-h, --help [this info]<br>
&nbsp;&nbsp;&nbsp;-s, --server, --target [target mail server]<br>
&nbsp;&nbsp;&nbsp;-p, --port [target port]<br>
&nbsp;&nbsp;&nbsp;-t, --to, --recipient [recipient]<br>
&nbsp;&nbsp;&nbsp;-f, --from, --sender [sender]<br>
&nbsp;&nbsp;&nbsp;-x, --xm, --x-mailer [X-Mailer header]<br>
&nbsp;&nbsp;&nbsp;--mix, --mixed [use multipart/mixed instead of multipart/alternative]<br>
&nbsp;&nbsp;&nbsp;--to-header [to: header if different from recipient]<br>
&nbsp;&nbsp;&nbsp;--from-header [from: header if different from sender]<br>
&nbsp;&nbsp;&nbsp;--body-text [text body string]<br>
&nbsp;&nbsp;&nbsp;--body-html [html body string]<br>
&nbsp;&nbsp;&nbsp;--text-encode, --text-charset [character encoding for text section]<br>
&nbsp;&nbsp;&nbsp;--html-encode, --html-charset [character encoding for html section]<br>
&nbsp;&nbsp;&nbsp;--encode, --charset [character encoding for both text and html sections (overrides --text-encode/--text-charset/--html-encode/--html-charset)]<br>
&nbsp;&nbsp;&nbsp;--high, --low [message importance (default is medium)]<br>
&nbsp;&nbsp;&nbsp;--ssl, --tls [use ssl/tls]<br>
&nbsp;&nbsp;&nbsp;--url [include malicious url]<br>
&nbsp;&nbsp;&nbsp;--ssn [include ssn numbers]<br>
&nbsp;&nbsp;&nbsp;--av, --virus [include eicar test virus]<br>
&nbsp;&nbsp;&nbsp;--zip [include password protected zip file]<br>
&nbsp;&nbsp;&nbsp;--eml, --write [write email to eml file]<br>
&nbsp;&nbsp;&nbsp;--no-send [do not send email (implies --eml/--write)]<br>
&nbsp;&nbsp;&nbsp;--eml-name [email file name (implies --eml/--write)]<br>
&nbsp;&nbsp;&nbsp;--no-text [no text body]<br>
&nbsp;&nbsp;&nbsp;--no-html [no html body]<br>
&nbsp;&nbsp;&nbsp;--spam [generate test spam]<br>
&nbsp;&nbsp;&nbsp;--adult [generate test adult spam (overrides --spam)]<br>
&nbsp;&nbsp;&nbsp;--dbg, --debug [additional debug information]<br>
&nbsp;&nbsp;&nbsp;--text-body [text body from specified file]<br>
&nbsp;&nbsp;&nbsp;--html-body [html body from specified file]<br>
&nbsp;&nbsp;&nbsp;--attach [attach specified file]</p>