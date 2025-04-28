document
  .getElementById("codeForm")
  .addEventListener("submit", async function (e) {
    e.preventDefault();
    const code = document.getElementById("code").value;
    const lexer = document.getElementById("lexerSelect").value;
    const response = await fetch("/lex", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ code: code, lexer: lexer }),
    });
    const data = await response.json();
    const lexemeList = document.getElementById("lexemes");
    lexemeList.innerHTML = "";
    data.lexemes.forEach(function (lex) {
      const li = document.createElement("li");
      li.textContent = `${lex.type}: '${lex.value}' (Line: ${lex.line}, Column: ${lex.column})`;
      lexemeList.appendChild(li);
    });
  });