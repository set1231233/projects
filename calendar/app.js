$(Function () {
Function C() {
P();
Var E = H();
Var R = 0;
Var U = False;
L.Empty();
While (!U) {
If (S[R] == E[0].Weekday) {
U = True;
} Else {
L.Append('<Div Class="Blank"></Div>');
R++;
}
}
For (Var C = 0; C < 42 - R; C++) {
If (C >= E.Length) {
L.Append('<Div Class="Blank"></Div>');
} Else {
Var V = E[C].Day;
Var M = G(New Date(T, N - 1, V)) ? '<Div Class="Today">' : "<Div>";
L.Append(M + "" + V + "</Div>");
}
}
Var Y = O[N - 1];
A.Css("Background-Color", Y)
.Find("H1")
.Text(I[N - 1] + " " + T);
F.Find("Div").Css("Color", Y);
L.Find(".Today").Css("Background-Color", Y);
D();
}
Function H() {
Var E = [];
For (Var R = 1; R < V(T, N) + 1; R++) {
E.Push({ Day: R, Weekday: S[M(T, N, R)] });
}
Return E;
}
Function P() {
F.Empty();
For (Var E = 0; E < 7; E++) {
F.Append("<Div>" + S[E].Substring(0, 3) + "</Div>");
}
}
Function D() {
Var T;
Var N = $("#Calendar").Css("Width", E + "Px");
N.Find((T = "#Calendar_weekdays, #Calendar_content"))
.Css("Width", E + "Px")
.Find("Div")
.Css({
Width: E / 7 + "Px",
Height: E / 7 + "Px",
"Line-Height": E / 7 + "Px",
});
N.Find("#Calendar_header")
.Css({ Height: E * (1 / 7) + "Px" })
.Find('I[Class^="Icon-Chevron"]')
.Css("Line-Height", E * (1 / 7) + "Px");
}
Function V(E, T) {
Return New Date(E, T, 0).GetDate();
}
Function M(E, T, N) {
Return New Date(E, T - 1, N).GetDay();
}
Function G(E) {
Return Y(New Date()) == Y(E);
}
Function Y(E) {
Return E.GetFullYear() + "/" + (E.GetMonth() + 1) + "/" + E.GetDate();
}
Function B() {
Var E = New Date();
T = E.GetFullYear();
N = E.GetMonth() + 1;
}
Var E = 480;
Var T = 2013;
Var N = 9;
Var R = [];
Var I = [
"JANUARY",
"FEBRUARY",
"MARCH",
"APRIL",
"MAY",
"JUNE",
"JULY",
"AUGUST",
"SEPTEMBER",
"OCTOBER",
"NOVEMBER",
"DECEMBER",
];
Var S = [
"Sunday",
"Monday",
"Tuesday",
"Wednesday",
"Thursday",
"Friday",
"Saturday",
];
Var O = [
"#16a085",
"#1abc9c",
"#C0392b",
"#27ae60",
"#FF6860",
"#F39c12",
"#F1c40f",
"#E67e22",
"#2ecc71",
"#E74c3c",
"#D35400",
"#2c3e50",
];
Var U = $("#Calendar");
Var A = U.Find("#Calendar_header");
Var F = U.Find("#Calendar_weekdays");
Var L = U.Find("#Calendar_content");
B();
C();
A.Find('I[Class^="Icon-Chevron"]').On("Click", Function () {
Var E = $(This);
Var R = Function (E) {
N = E == "Next" ? N + 1 : N - 1;
If (N < 1) {
N = 12;
T--;
} Else If (N > 12) {
N = 1;
T++;
}
C();
};
If (E.Attr("Class").IndexOf("Left") != -1) {
R("Previous");
} Else {
R("Next");
}
});
});
