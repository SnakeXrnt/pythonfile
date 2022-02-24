


msg1 =msgbox("Hello Valen" ,0, "Jangan di close lho")
msg2 =msgbox("jadi" ,0, "Jangan di close lho")
msg3 =msgbox("aku cuman mau nanyo kau" ,0, "Jangan di close lho")
msg4 =msgbox("kaloooooooo" ,0, "Jangan di close lho")
intAnswer = _
    Msgbox("", _
        vbYesNo, "Delete Files")
If intAnswer = vbYes Then
    Msgbox "You answered yes."
Else
    Msgbox "You answered no."
End If
