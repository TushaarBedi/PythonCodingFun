Sub challenge1():

' Set Dimensions
Dim ws As Worksheet
Dim total As Double
Dim j As Integer

    For Each ws In Worksheets
    ' Set variables for each sheet
    total = 0
    j = 0

    ' Set title rows
    ws.Range("I1").Value = "Ticker"
    ws.Range("J1").Value = "Total Stock Volume"

    ' get the row number of the last row with data
    rowCount = Cells(Rows.Count, "A").End(xlUp).Row

        For i = 2 To rowCount

            ' If ticker changes then print results
            If ws.Cells(i + 1, 1).Value <> ws.Cells(i, 1).Value Then

                ' Stores results in variable
                total = total + ws.Cells(i, 7).Value
            
                ' Print ticker symbol
                ws.Range("I" & 2 + j).Value = ws.Cells(i, 1).Value

                ' Print total
                ws.Range("J" & 2 + j).Value = total

                ' Reset Total
                total = 0
                ' Move to next row
                j = j + 1

            ' Else keep adding to the total volume
            Else
                total = total + ws.Cells(i, 7).Value

            End If

        Next i
        ' reset variable in worksheet
        total = 0
        j = 0

    Next ws

End Sub
