Sub stock_analysis():

' Set dimensions
Dim total As Double
Dim i As Long
Dim change As Single
Dim j As Integer
Dim start As Long
Dim rowCount As Long
Dim percentChange As Single
Dim days As Integer
Dim dailyChange As Single
Dim averageChange As Single

' Set title row
Range("I1").Value = "Ticker"
Range("J1").Value = "Yearly Change"
Range("K1").Value = "Percent Change"
Range("L1").Value = "Total Stock Volume"


' Set initial values
j = 0
total = 0
change = 0
start = 2

' get the row number of the last row with data
rowCount = Cells(Rows.Count, "A").End(xlUp).Row

For i = 2 To rowCount

' If ticker changes then print results
    If Cells(i + 1, 1).Value <> Cells(i, 1).Value Then

        ' Stores results in variables
        total = total + Cells(i, 7).Value

        ' Handle zero total volume
        If total = 0 Then
            ' print the results
            Range("I" & 2 + j).Value = Cells(i, 1).Value
            Range("J" & 2 + j).Value = 0
            Range("K" & 2 + j).Value = "%" & 0
            Range("L" & 2 + j).Value = 0
        Else
            
            ' Find First non zero starting value
            If Cells(start, 3) = 0 Then
                For find_value = start To i
                    If Cells(find_value, 3).Value <> 0 Then
                     
                        start = find_value
                        Exit For
                    End If
                 Next find_value
            End If

            ' Calculate Change
            change = (Cells(i, 6) - Cells(start, 3))
            percentChange = Round((change / Cells(start, 3) * 100), 2)

            ' start of the next stock ticker
            start = i + 1

            ' print the results
            Range("I" & 2 + j).Value = Cells(i, 1).Value
            Range("J" & 2 + j).Value = Round(change, 2)
            Range("K" & 2 + j).Value = "%" & percentChange
            Range("L" & 2 + j).Value = total


            ' colors positives green and negatives red
            Select Case change
                Case Is > 0
                Range("J" & 2 + j).Interior.ColorIndex = 4
                Case Is < 0
                    Range("J" & 2 + j).Interior.ColorIndex = 3
                Case Else
                    Range("J" & 2 + j).Interior.ColorIndex = 0
            End Select

        End If


        ' reset variables for new stock ticker
        total = 0
        change = 0
        j = j + 1
        days = 0


   ' If ticker is still the same add results
    Else

        total = total + Cells(i, 7).Value

    End If

Next i

End Sub
