
class M-O_WebInterface:
    def __init__(self):
        

    def webpage(self, dist):
        CSS = self.getCSS()
        CONTROL = self.controlTable()
        MOVES = self.movesTable()
        GESTURES = self.gesturesTable()
        #Template HTML
        html = f"""
                <!DOCTYPE html>
                <html>
                <head>
                <style>
                {CSS}
                </style>
                </head>
                <body>
                <div align = "center">
                <h1>Mini Otto</h1>
                {CONTROL}                
                <table align = "center">
                    <tr><td align = "center"> 
                        {MOVES}
                    </td><td align = "center">
                        {SONGS}
                    </td></tr>
                </table>
                {GESTURES} 
                </div>
                </body>
                </html>
                """
        return str(html)
    
    def BLANKpage(self, dist):
        CSS = self.getCSS()
        #Template HTML
        html = f"""
                <!DOCTYPE html>
                <html>
                <head>
                <style>
                {CSS}
                </style>
                </head>
                <body>
                <div align = "center">
                <h1>Mini Otto</h1>
                PLEASE WAIT A TIC
                </div>
                </body>
                </html>
                """
        return str(html)
    
    
    def getCSS(self):
        css = "
         body {{
                color:#eae0c2;
                background-color: #1c1b18;
                font-family:Arial;
                font-size:14px;
                font-weight:bold;
            }}
  
            input {{
                box-shadow: 0px 1px 0px 0px #1c1b18;
                background:linear-gradient(to bottom, #eae0c2 5%, #ccc2a6 100%);
                background-color:#eae0c2;
                border-radius:15px;
                border:2px solid #333029;
                display:inline-block;
                cursor:pointer;
                color:#505739;
                font-family:Arial;
                font-size:14px;
                font-weight:bold;
                padding:12px 16px;
                text-decoration:none;
                text-shadow:0px 1px 0px #ffffff;
                width: 146px
            }}
            input:hover {{
                background:linear-gradient(to bottom, #ccc2a6 5%, #eae0c2 100%);
                background-color:#ccc2a6;
            }}
            input:active {{
                position:relative;
                top:1px;
            }}     
     
            .direction {{
                color:#FF00FF;
                font-size:20px;
                width: 50px;
            }}
            
            .gesture {{
                color:#FF0000;
            }}
            .move {{
                color:#00AF00;
            }}
            .song {{
                color:#0000FF;
            }}
            .control {{
                color:#FF00FF;
            }}
            "
        return str(css)
    
    def controlTable():
        control = "
          <h3 class='control'>Control</h3>
          <table><tr><td>            
           
            <table><tr><td>&nbsp;</td>
              <td><form action='./FW'><input type='submit' value='&uarr;' class='direction' /></form></td>
              <td>&nbsp;</td>
              </tr><tr>
              <td><form action='./L'><input type='submit' value='&larr;' class='direction' /></form></td>
              <td><form action='./STP'><input type='submit' value='&excl;' class='direction' /></form></td>
              <td><form action='./R'><input type='submit' value='&rarr;' class='direction' /></form></td>
              </tr><tr>
              <td>&nbsp;</td>
              <td><form action='./BK'><input type='submit' value='&darr;' class='direction' /></form></td>
              <td>&nbsp;</td>
              </tr>
            </table>
          </td>
          <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
          <td align = 'center'>
                &nbsp;&nbsp;&nbsp;&nbsp;Distance: {dist} cm &nbsp;&nbsp;&nbsp; <form action='./UPD'><input type='submit' value='Refresh' /></form>
           </td>
            </tr>
        </table>
        "
    
    def movesTable(self):
        moves = "
        <h3 class='move'>Moves</h3>
                  <table><tr>
                  <td><form action='./M-F'><input type='submit' value='Forward' class='move' /></form></td>
                  <td><form action='./M-B'><input type='submit' value='Backward' class='move' /></form></td>
                  <td><form action='./M-TL'><input type='submit' value='Turn Left' class='move' /></form></td>
                  </tr><tr>
                  <td><form action='./M-TR'><input type='submit' value='Turn Right' class='move' /></form></td>
                  <td><form action='./M-BL'><input type='submit' value='Bend Left' class='move' /></form></td>
                  <td><form action='./M-BR'><input type='submit' value='Bend Right' class='move' /></form></td>
                  </tr><tr>
                  <td><form action='./M-SL'><input type='submit' value='Shake Left Leg' class='move' /></form></td>
                  <td><form action='./M-SR'><input type='submit' value='Shake Right Leg' class='move' /></form></td>
                  <td><form action='./M-ML'><input type='submit' value='Moonwalk Left' class='move' /></form></td>
                  </tr><tr>
                  <td><form action='./M-MR'><input type='submit' value='Moonwalk Right' class='move' /></form></td>
                  <td><form action='./M-CL'><input type='submit' value='Crusaito Left' class='move' /></form></td>
                  <td><form action='./M-CR'><input type='submit' value='Crusaito Right' class='move' /></form></td>
                  </tr><tr>
                  <td><form action='./M-FL'><input type='submit' value='Flapping Left' class='move' /></form></td>
                  <td><form action='./M-FR'><input type='submit' value='Flapping Right' class='move' /></form></td>
                  <td><form action='./M-SW'><input type='submit' value='Swing' class='move' /></form></td>
                  </tr><tr>
                  <td><form action='./M-TS'><input type='submit' value='Tiptoe Swing' class='move' /></form></td>
                  <td><form action='./M-JI'><input type='submit' value='Jitter' class='move' /></form></td>
                  <td><form action='./M-UD'><input type='submit' value='Up Down' class='move' /></form></td>
                  </tr><tr>
                  <td><form action='./M-AT'><input type='submit' value='Ascending Turn' class='move' /></form></td>
                  <td>&nbsp;</td>
                  <td><form action='./M-JU'><input type='submit' value='Jump' class='move' /></form></td>
                  </tr></table>
        "
        return moves
        
    def songsTable(self):
        songs = "
         <h3 class='song'>Songs</h3>
                  <table><tr>
                  <td><form action='./S-0'><input type='submit' value='Connection' class='song' /></form></td>
                  <td><form action='./S-1'><input type='submit' value='Disconnection' class='song' /></form></td>
                  <td><form action='./S-2'><input type='submit' value='Suprise' class='song' /></form></td>
                  </tr><tr>
                  <td><form action='./S-3'><input type='submit' value='Ohooh' class='song' /></form></td>
                  <td><form action='./S-4'><input type='submit' value='Ohooh 2' class='song' /></form></td>
                  <td><form action='./S-5'><input type='submit' value='Cuddly' class='song' /></form></td>
                  </tr><tr>
                  <td><form action='./S-6'><input type='submit' value='Sleeping' class='song' /></form></td>
                  <td><form action='./S-7'><input type='submit' value='Happy' class='song' /></form></td>
                  <td><form action='./S-8'><input type='submit' value='Super Happy' class='song' /></form></td>
                  </tr><tr>
                  <td><form action='./S-9'><input type='submit' value='Happy Short' class='song' /></form></td>
                  <td><form action='./S-10'><input type='submit' value='Sad' class='song' /></form></td>
                  <td><form action='./S-11'><input type='submit' value='Confused' class='song' /></form></td>
                  </tr><tr>
                  <td><form action='./S-12'><input type='submit' value='Fart 1' class='song' /></form></td>
                  <td><form action='./S-13'><input type='submit' value='Fart 2' class='song' /></form></td>
                  <td><form action='./S-14'><input type='submit' value='Fart 3' class='song' /></form></td>
                  </tr><tr>
                  <td><form action='./S-15'><input type='submit' value='Mode 1' class='song' /></form></td>
                  <td><form action='./S-16'><input type='submit' value='Mode 2' class='song' /></form></td>
                  <td><form action='./S-17'><input type='submit' value='Mode 3' class='song' /></form></td>
                  </tr><tr>
                  <td>&nbsp;</td>
                  <td><form action='./S-18'><input type='submit' value='Button Pressed' class='song' /></form></td>
                  <td>&nbsp;</td>
                  </tr></table>
        "
        return songs
    
    def gesturesTable(self):
        gestures = "
         <h3  class='gesture'>Gestures</h3>
                <table><tr>
                <td><form action='./G-H'><input type='submit' value='Happy' class='gesture'/></form></td>
                <td><form action='./G-SH'><input type='submit' value='Super Happy' class='gesture' /></form></td>
                <td><form action='./G-S'><input type='submit' value='Sad' class='gesture' /></form></td>
                </tr><tr>
                <td><form action='./G-SL'><input type='submit' value='Sleeping' class='gesture' /></form></td>
                <td><form action='./G-FT'><input type='submit' value='Fart' class='gesture' /></form></td>
                <td><form action='./G-C'><input type='submit' value='Confused' class='gesture' /></form></td>
                </tr><tr>
                <td><form action='./G-L'><input type='submit' value='Love' class='gesture' /></form></td>
                <td><form action='./G-A'><input type='submit' value='Angry' class='gesture' /></form></td>
                <td><form action='./G-F'><input type='submit' value='Fretful' class='gesture' /></form></td>
                </tr><tr>
                <td><form action='./G-M'><input type='submit' value='Magic' class='gesture' /></form></td>
                <td><form action='./G-W'><input type='submit' value='Wave' class='gesture' /></form></td>
                <td><form action='./G-V'><input type='submit' value='Victory' class='gesture' /></form></td>
                </tr><tr>
                <td>&nbsp;</td>
                <td><form action='./G-FL'><input type='submit' value='Fail' class='gesture' /></form></td>
                <td>&nbsp;</td>
                </tr></table>      
        "
        return gestures