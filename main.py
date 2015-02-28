import node

blocks = '<br><small>&nbsp;' + node.blocks + ' | ' + node.lastblock + '&nbsp;</small>'
difficulty = '<br>&nbsp;' + node.difficulty + '&nbsp;</br>'
connections = '<br>&nbsp;' + node.connections + '&nbsp;</br>'
softver = '<br>&nbsp;' + node.soft_ver + ' | ' + node.prot_ver + '&nbsp;</br>'
sysdatatime = '<br>&nbsp;' + node.systemtime + '&nbsp;</br>'
systemhost = '<br>&nbsp;' + node.systemhost + '&nbsp;</br>'
inf_block = '''
            <p><small>&nbsp; Hash:&nbsp;''' + node.hashblock + '''</small></p>
            <p><small>&nbsp; Tx Count:&nbsp;''' + node.txcount + '''</small></p>
            <p><small>&nbsp; Block Size:&nbsp;''' + node.sizeblock + '''</small></p>
            <p><small>&nbsp; Date & Time:&nbsp;''' + node.timeblock + '''</small></p>
            '''
tips =  '''
            <p class="text-center">
                <br>&nbsp;</br>
                <small><em>If you like this, please consider a contribution ->&nbsp;<em></small>
                <button type="button" class="btn btn-default btn-lg" data-toggle="modal" data-target="#blocktips"><span class="glyphicon glyphicon-qrcode" aria-hidden="true"></span></button>
                    <div class="modal fade" id="blocktips" tabindex="-1" role="dialog" aria-labelledby="ModalLabel" aria-hidden="true">
                        <div class="modal-dialog">
                            <div class="modal-content">
                                <div class="modal-header">
                                    <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                                    <h4 class="modal-title"> * Scan & Tip </h4>
                                </div>
                                <div class="modal-body text-center">
                                    <img src="./img/qr.png" alt="address">
                                    <p>&nbsp;</p>
                                    <strong>19jFVjhkhJqWS8ngNxQ5rFjhnvjroXWFqU</strong>
                                </div>
                                <div class="modal-footer"></div>
                            </div>
                        </div>
                    </div>
            </p>
        '''
powered =   '''
                <p class="text-center">   
                    <a href="http://getbootstrap.com/" target="_blank" style:"border-style: none;"><img src="./img/bootstrap-solid.svg" height="40px" alt="Bootstrap"></a>      
                    <a href="https://www.python.org/" target="_blank" style:"border-style: none;"><img src="./img/python-logo.png" height="50px" alt="python"></a>
                    <em> of course with </em>
                    <a href="http://www.bitcoin.org/" target="_blank" style:"border-style: none;"><img src="./img/bitcoin-logo.svg" height="45px" alt="Bitcoin"></a>
                    <em> and thanks to everyone than support the Bitcoin Networks.</em> 
                </p>      
            '''
webdoc='''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="Bitcoin Node Information">
    <meta name="author" content="@luisan00">
    <link rel="icon" href="../../favicon.ico">
    <title>Webit</title>
    <!-- Bootstrap core CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css"> 
      <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->
</head>
<body style="padding-top: 70px;">
    <div class="container container-fluid">
        <nav class="navbar navbar-default navbar-fixed-top" role="navigation">
            <div class="navbar-header"><a class="navbar-brand"><img alt="PyNode" src="./img/headbar.png" height="50px" href="#"></a></div>
        </nav>
        <div class="row marketing">
            <div class="col-xs-6"><!-- left panels -->
                <div class="panel panel-default">
                    <div class="panel-heading"><em>Proccessed blocks</em></div> 
                    <div class="panel-body"> '''+ blocks + ''' 
                        <button type="button" class="btn btn-default btn-xs" data-toggle="modal" data-target="#blockmodal"><span class="glyphicon glyphicon-new-window" aria-hidden="true"></span></button></br>
                    </div>
                    <div class="modal fade" id="blockmodal" tabindex="-1" role="dialog" aria-labelledby="ModalLabel" aria-hidden="true">
                        <div class="modal-dialog">
                            <div class="modal-content">
                                <div class="modal-header">
                                    <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                                    <h4 class="modal-title"> Block: ''' + node.heightblock + '''</h4>
                                </div>
                                <div class="modal-body">'''+ inf_block + '''</div>
                                <div class="modal-footer"><button type="button" class="btn btn-primary"><em>More</em></button></div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="panel panel-default">
                    <div class="panel-heading"><em>Difficulty</em></div>
                    <div class="panel-body"> '''+ difficulty +'''</div>
                </div>
                <div class="panel panel-default">
                    <div class="panel-heading"><em>Connections</em></div>
                    <div class="panel-body">''' + connections + '''</div>
                </div>
            </div><!-- left panels -->
            <div class="col-xs-6"><!-- right panels -->
                <div class="panel panel-default">
                    <div class="panel-heading"><em>Software Version&nbsp;|&nbsp;Protocol Version</em></div>
                    <div class="panel-body">'''+ softver + '''</div>
                </div>
                <div class="panel panel-default">
                    <div class="panel-heading"><em>System Date & Time</em></div>
                    <div class="panel-body">''' + sysdatatime + '''</div>
                </div>
                <div class="panel panel-default">
                  <div class="panel-heading"><em>System Host</em></div>
                  <div class="panel-body">''' + systemhost + '''</div>
                </div> 
            </div><!-- right panels -->            
        </div><!-- row marketing -->
    <div class="panel panel-default"> <!-- bottom panel -->  
        <p class="text-center"><strong><em>Run by:</em></strong></p>
        '''+ powered + '''
    </div> <!-- bottom panel --> 
    <div class="panel panel-default">''' + tips +  '''</div>      
    <footer class="footer">
        <div>
            <p class="text-center"><small>Designed and built by</small>
                <a href="https://twitter.com/luisan00" target="_blank"><small>&nbsp;@luisan00</small></a>
            </p>
            <p class="text-center"><small>Code licensed under</small>
                <a href="https://raw.githubusercontent.com/luisan00/webit/master/LICENSE" target="_blank"><small>&nbsp;MIT</small></a>
                <small>, documentation under</small>
                <a  href="http://creativecommons.org/licenses/by/4.0/" target="_blank"><small>&nbsp;CC BY 4.0.</small></a>
            </p>
        </div>
    </footer>
   </div> <!-- /container -->
    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/js/bootstrap.min.js"></script>
  </body>
</html>
    '''
buff = open('./documents/static/index.htm', 'w')
buff.write(webdoc)
buff.close()
print 'ready!'
