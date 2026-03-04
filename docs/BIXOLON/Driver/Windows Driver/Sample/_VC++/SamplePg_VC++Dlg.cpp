
// SamplePg_VC++Dlg.cpp : implementation file
//

#include "stdafx.h"
#include "SamplePg_VC++.h"
#include "SamplePg_VC++Dlg.h"


// Link bixolon library
#include ".\\Inc\\BXLPDcApi.h"

#ifdef TARGET_64BIT
#pragma comment(lib, ".\\Lib\\BXLPDC_x64.lib")
#else
#pragma comment(lib, ".\\Lib\\BXLPDC.lib")
#endif



//	Cash Draw Speed
#define	 SPEED_50MS				0
#define	 SPEED_100MS			1
#define	 SPEED_150MS			2
#define	 SPEED_200MS			3
#define	 SPEED_250MS			4

#ifdef _DEBUG
#define new DEBUG_NEW
#endif


// CSamplePg_VCDlg dialog


CSamplePg_VCDlg::CSamplePg_VCDlg(CWnd* pParent /*=NULL*/)
	: CDialog(CSamplePg_VCDlg::IDD, pParent)
	, m_strPrinterName(_T(""))
{
	m_hIcon = AfxGetApp()->LoadIcon(IDR_MAINFRAME);
}

void CSamplePg_VCDlg::DoDataExchange(CDataExchange* pDX)
{
	CDialog::DoDataExchange(pDX);
	DDX_Control(pDX, IDC_COMBO_DEVICEFONT, m_cmbDeviceFont);
	DDX_Text(pDX, IDC_EDIT_PRINTERNAME, m_strPrinterName);
	DDX_Control(pDX, IDC_COMBO_CASHDRAWER_SPEED, m_cmbCashdrawer_Speed);
}

BEGIN_MESSAGE_MAP(CSamplePg_VCDlg, CDialog)
	ON_WM_PAINT()
	ON_WM_QUERYDRAGICON()
	//}}AFX_MSG_MAP
	ON_BN_CLICKED(IDC_CONNECT, &CSamplePg_VCDlg::OnBnClickedConnect)
	ON_BN_CLICKED(IDC_DISCONNECT, &CSamplePg_VCDlg::OnBnClickedDisconnect)
	ON_BN_CLICKED(IDC_PRINT_DEVICEFONT, &CSamplePg_VCDlg::OnBnClickedPrintDevicefont)
	ON_WM_DESTROY()
	ON_BN_CLICKED(IDC_PARTIALCUT, &CSamplePg_VCDlg::OnBnClickedPartialcut)
	ON_BN_CLICKED(IDC_PARTIALCUT_NOFEED, &CSamplePg_VCDlg::OnBnClickedPartialcutNofeed)
	ON_BN_CLICKED(IDC_PRINT_RECEIPT, &CSamplePg_VCDlg::OnBnClickedPrintReceipt)
	ON_BN_CLICKED(IDCANCEL, &CSamplePg_VCDlg::OnBnClickedCancel)
	ON_BN_CLICKED(IDC_CASHDRAWER_OPEN, &CSamplePg_VCDlg::OnBnClickedCashdrawerOpen)
END_MESSAGE_MAP()


// CSamplePg_VCDlg message handlers

BOOL CSamplePg_VCDlg::OnInitDialog()
{
	CDialog::OnInitDialog();

	// Set the icon for this dialog.  The framework does this automatically
	//  when the application's main window is not a dialog
	SetIcon(m_hIcon, TRUE);			// Set big icon
	SetIcon(m_hIcon, FALSE);		// Set small icon

	// TODO: Add extra initialization here

	// FontA
	m_cmbDeviceFont.AddString(TEXT("FontA1x1"));
	m_cmbDeviceFont.AddString(TEXT("FontA1x1[255]"));
	m_cmbDeviceFont.AddString(TEXT("FontA1x1[Ext.]"));
	m_cmbDeviceFont.AddString(TEXT("FontA1x2"));
	m_cmbDeviceFont.AddString(TEXT("FontA1x2[255]"));
	m_cmbDeviceFont.AddString(TEXT("FontA1x2[Ext.]"));
	m_cmbDeviceFont.AddString(TEXT("FontA2x1"));
	m_cmbDeviceFont.AddString(TEXT("FontA2x1[255]"));
	m_cmbDeviceFont.AddString(TEXT("FontA2x1[Ext.]"));
	m_cmbDeviceFont.AddString(TEXT("FontA2x2"));
	m_cmbDeviceFont.AddString(TEXT("FontA2x2[255]"));
	m_cmbDeviceFont.AddString(TEXT("FontA2x2[Ext.]"));

	// FontB
	m_cmbDeviceFont.AddString(TEXT("FontB1x1"));
	m_cmbDeviceFont.AddString(TEXT("FontB1x1[255]"));
	m_cmbDeviceFont.AddString(TEXT("FontB1x1[Ext.]"));
	m_cmbDeviceFont.AddString(TEXT("FontB1x2"));
	m_cmbDeviceFont.AddString(TEXT("FontB1x2[255]"));
	m_cmbDeviceFont.AddString(TEXT("FontB1x2[Ext.]"));
	m_cmbDeviceFont.AddString(TEXT("FontB2x1"));
	m_cmbDeviceFont.AddString(TEXT("FontB2x1[255]"));
	m_cmbDeviceFont.AddString(TEXT("FontB2x1[Ext.]"));
	m_cmbDeviceFont.AddString(TEXT("FontB2x2"));
	m_cmbDeviceFont.AddString(TEXT("FontB2x2[255]"));
	m_cmbDeviceFont.AddString(TEXT("FontB2x2[Ext.]"));

	// Korean fonts
	m_cmbDeviceFont.AddString(TEXT("Korean1x1"));
	m_cmbDeviceFont.AddString(TEXT("Korean1x2"));
	m_cmbDeviceFont.AddString(TEXT("Korean2x1"));
	m_cmbDeviceFont.AddString(TEXT("Korean2x2"));

	// Chinese fonts
	m_cmbDeviceFont.AddString(TEXT("Chinese2312_1x1"));
	m_cmbDeviceFont.AddString(TEXT("Chinese2312_1x2"));
	m_cmbDeviceFont.AddString(TEXT("Chinese2312_2x1"));
	m_cmbDeviceFont.AddString(TEXT("Chinese2312_2x2"));

	m_cmbDeviceFont.AddString(TEXT("ChineseBIG5_1x1"));
	m_cmbDeviceFont.AddString(TEXT("ChineseBIG5_1x2"));
	m_cmbDeviceFont.AddString(TEXT("ChineseBIG5_2x1"));
	m_cmbDeviceFont.AddString(TEXT("ChineseBIG5_2x2"));

	m_cmbDeviceFont.SetCurSel(0);

	// Adding string for Cash drawer.
	m_cmbCashdrawer_Speed.AddString(TEXT("50ms"));
	m_cmbCashdrawer_Speed.AddString(TEXT("100ms"));
	m_cmbCashdrawer_Speed.AddString(TEXT("150ms"));
	m_cmbCashdrawer_Speed.AddString(TEXT("200ms"));
	m_cmbCashdrawer_Speed.AddString(TEXT("250ms"));

	m_cmbCashdrawer_Speed.SetCurSel(0);

	//	Initialize Cash Draw Number
	((CButton*)GetDlgItem(IDC_RADIO_CASHDRAWER_1))->SetCheck(TRUE);

	// Initialize Printer Name
	m_strPrinterName = TEXT("BIXOLON SRP-275III");

	UpdateData(FALSE);

	return TRUE;  // return TRUE  unless you set the focus to a control
}

// If you add a minimize button to your dialog, you will need the code below
//  to draw the icon.  For MFC applications using the document/view model,
//  this is automatically done for you by the framework.

void CSamplePg_VCDlg::OnPaint()
{
	if (IsIconic())
	{
		CPaintDC dc(this); // device context for painting

		SendMessage(WM_ICONERASEBKGND, reinterpret_cast<WPARAM>(dc.GetSafeHdc()), 0);

		// Center icon in client rectangle
		int cxIcon = GetSystemMetrics(SM_CXICON);
		int cyIcon = GetSystemMetrics(SM_CYICON);
		CRect rect;
		GetClientRect(&rect);
		int x = (rect.Width() - cxIcon + 1) / 2;
		int y = (rect.Height() - cyIcon + 1) / 2;

		// Draw the icon
		dc.DrawIcon(x, y, m_hIcon);
	}
	else
	{
		CDialog::OnPaint();
	}
}

// The system calls this function to obtain the cursor to display while the user drags
//  the minimized window.
HCURSOR CSamplePg_VCDlg::OnQueryDragIcon()
{
	return static_cast<HCURSOR>(m_hIcon);
}

void CSamplePg_VCDlg::EnableCtrls(BOOL bConnect)
{
	GetDlgItem(IDC_CONNECT)->EnableWindow(!bConnect);
	GetDlgItem(IDC_EDIT_PRINTERNAME)->EnableWindow(!bConnect);

	GetDlgItem(IDC_DISCONNECT)->EnableWindow(bConnect);

	m_cmbDeviceFont.EnableWindow(bConnect);
	GetDlgItem(IDC_PRINT_DEVICEFONT)->EnableWindow(bConnect);

	m_cmbCashdrawer_Speed.EnableWindow(bConnect);
	GetDlgItem(IDC_RADIO_CASHDRAWER_1)->EnableWindow(bConnect);
	GetDlgItem(IDC_RADIO_CASHDRAWER_2)->EnableWindow(bConnect);
	GetDlgItem(IDC_CASHDRAWER_OPEN)->EnableWindow(bConnect);

	GetDlgItem(IDC_PARTIALCUT)->EnableWindow(bConnect);
	GetDlgItem(IDC_PARTIALCUT_NOFEED)->EnableWindow(bConnect);
	GetDlgItem(IDC_PRINT_RECEIPT)->EnableWindow(bConnect);

	UpdateData(FALSE);
}

void CSamplePg_VCDlg::OnBnClickedConnect()
{
	UpdateData(TRUE);

	if(ConnectPrinterW(m_strPrinterName.GetBuffer(m_strPrinterName.GetLength()))) {
		EnableCtrls(TRUE);
	}
}

void CSamplePg_VCDlg::OnBnClickedDisconnect()
{
	DisconnectPrinter();

	EnableCtrls(FALSE);
}

void CSamplePg_VCDlg::OnBnClickedPrintDevicefont()
{
	TCHAR	szFontName[32]	= {NULL, }; 
	CString	strBuffer		= TEXT("");
	INT		nFontSize		= 0;
	INT		nPositionY		= 0;

	UpdateData(TRUE);

	// Start Document
	if(Start_DocW(TEXT("Print Device Font"))) 
	{		
		Start_Page();	// Start Page

		m_cmbDeviceFont.GetLBText(m_cmbDeviceFont.GetCurSel(), szFontName);

		nFontSize = 9;

		if(_tcsstr(szFontName, TEXT("Font")))
		{
			if(_tcsstr(szFontName, TEXT("x2")))
				nFontSize = 18;
			else
				nFontSize = 9;
		}
		else
		{
			if(_tcsstr(szFontName, TEXT("x2")))
				nFontSize = 32;
			else
				nFontSize = 16;
		}

		// Font name.
		strBuffer.Format(TEXT("FontName : %s"), szFontName);
		nPositionY += PrintDeviceFontW(0, nPositionY, szFontName, nFontSize, strBuffer.GetBuffer(strBuffer.GetLength()));

		// Text to print.
		strBuffer.Format(TEXT("TEST"));
		nPositionY += PrintDeviceFontW(0, nPositionY, szFontName, nFontSize, strBuffer.GetBuffer(strBuffer.GetLength()));

		End_Page();		// End Page
		End_Doc();		// End Document
	}
}

void CSamplePg_VCDlg::OnDestroy()
{
	CDialog::OnDestroy();

	DisconnectPrinter();
}

void CSamplePg_VCDlg::OnBnClickedPartialcut()
{
	int nPositionX	= 0;	
	int	nPositionY	= 0;
	int	nTextHeight	= 0;

	UpdateData(TRUE);

	// Start Document
	if(Start_DocW(TEXT("Partial Cut"))) 
	{
		Start_Page();	// Start Page

		nPositionY += nTextHeight;
		nTextHeight = PrintDeviceFontW(nPositionX, nPositionY, TEXT("FontControl"), 9, TEXT("P"));

		End_Page();		// End Page
		End_Doc();		// End Document
	}
}

void CSamplePg_VCDlg::OnBnClickedPartialcutNofeed()
{
	int	nPositionX	= 0;	
	int	nPositionY	= 0;
	int	nTextHeight	= 0;

	UpdateData(TRUE);

	// Start Document
	if(Start_DocW(TEXT("Partial Cut without feeds"))) 
	{
		Start_Page();	// Start Page

		nPositionY += nTextHeight;
		nTextHeight = PrintDeviceFontW(nPositionX, nPositionY, TEXT("FontControl"), 9, TEXT("g"));
		//nTextHeight = PrintDeviceFontW(nPositionX, nPositionY, TEXT("FontControl"), 9, TEXT("f"));
		//nTextHeight = PrintDeviceFontW(nPositionX, nPositionY, TEXT("FontControl"), 9, TEXT("F"));

		End_Page();		// End Page
		End_Doc();		// End Document
	}
}

void CSamplePg_VCDlg::OnBnClickedPrintReceipt()
{
	int			nPositionX	= 0;	
	int			nPositionY	= 0;
	int			nTextHeight	= 0;
	CString		strBuffer	= _T("");

	UpdateData(TRUE);

	// Start Document
	if( Start_Doc("Print Receipt") == FALSE ) 
		return;
	// Start Page
	Start_Page();

	nPositionY += nTextHeight;
	nTextHeight = PrintDeviceFontW(nPositionX, nPositionY, TEXT("FontControl"), 9, TEXT("x"));		// ALIGNS TEXT TO THE CENTER

	nPositionY += nTextHeight;
	nTextHeight = PrintDeviceFontW(nPositionX, nPositionY, TEXT("FontA2x2"), 18, TEXT("* BIXOLON CAFE *"));

	nPositionY += nTextHeight;
	nTextHeight = PrintDeviceFontW(nPositionX, nPositionY, TEXT("FontA1x1"), 9, TEXT("Bundang-gu, Seongam-si"));

	nPositionY += nTextHeight;
	nTextHeight = PrintDeviceFontW(nPositionX, nPositionY, TEXT("FontA1x1"), 9, TEXT("Sampyeong-dong, 685"));

	nPositionY += nTextHeight;
	nTextHeight = PrintDeviceFontW(nPositionX, nPositionY, TEXT("FontA1x1"), 9, TEXT("Tel) 858-519-3698 Fax) 3852"));

	nPositionY += nTextHeight;
	nTextHeight = PrintDeviceFontW(nPositionX, nPositionY, TEXT("FontControl"), 9, TEXT("w"));	// ALIGNS TEXT TO THE LEFT

	nPositionY += nTextHeight*2;
	nTextHeight = PrintDeviceFontW(nPositionX, nPositionY, TEXT("FontA1x1"), 9, TEXT("------------------------------"));

	nPositionY += nTextHeight;
	nTextHeight = PrintDeviceFontW(nPositionX, nPositionY, TEXT("FontA1x1"), 9, TEXT("ORANGE                  $3,500"));

	nPositionY += nTextHeight;
	nTextHeight = PrintDeviceFontW(nPositionX, nPositionY, TEXT("FontA1x1"), 9, TEXT("BUFALO WING             $3,000"));

	nPositionY += nTextHeight;
	nTextHeight = PrintDeviceFontW(nPositionX, nPositionY, TEXT("FontA1x1"), 9, TEXT("POTATO                  $1,200"));

	nPositionY += nTextHeight;
	nTextHeight = PrintDeviceFontW(nPositionX, nPositionY, TEXT("FontA1x1"), 9, TEXT("------------------------------"));

	nPositionY += nTextHeight;
	nTextHeight = PrintDeviceFontW(nPositionX, nPositionY, TEXT("FontA1x1"), 9, TEXT("Total                   $7,700"));

	nPositionY += nTextHeight;
	nTextHeight = PrintDeviceFontW(nPositionX, nPositionY, TEXT("FontA1x1"), 9, TEXT("Tax 6%                    $470"));

	nPositionY += nTextHeight;
	nTextHeight = PrintDeviceFontW(nPositionX, nPositionY, TEXT("FontA1x1"), 9, TEXT("Member Discount           $900"));

	nPositionY += nTextHeight;
	nTextHeight = PrintDeviceFontW(nPositionX, nPositionY, TEXT("FontA1x1"), 9, TEXT("Money received         $10,000"));

	nPositionY += nTextHeight;
	nTextHeight = PrintDeviceFontW(nPositionX, nPositionY, TEXT("FontA1x1"), 9, TEXT("Change                  $2,730"));

	nPositionY += nTextHeight;
	nTextHeight = PrintDeviceFontW(nPositionX, nPositionY, TEXT("FontA1x1"), 9, TEXT("------------------------------"));

	nPositionY += nTextHeight;
	nTextHeight = PrintDeviceFontW(nPositionX, nPositionY, TEXT("FontControl"), 9, TEXT("x"));		// ALIGNS TEXT TO THE CENTER

	nPositionX  = 25;
	nPositionY += nTextHeight/2;
	nTextHeight = PrintTrueFontW(nPositionX, nPositionY, TEXT("Arial"), 10, TEXT("Member Number : 452331949"), FALSE, 0, TRUE);

	nPositionY += nTextHeight;
	nTextHeight = PrintTrueFontW(nPositionX, nPositionY, TEXT("Arial"), 10, TEXT("HAVE A NICE DAY!"), FALSE, 0, TRUE);

	nPositionY += nTextHeight;
	nTextHeight = PrintTrueFontW(nPositionX, nPositionY, TEXT("Arial"), 10, TEXT("Sale Date: 07/01/03"), FALSE, 0, TRUE);

	nPositionY += nTextHeight;
	nTextHeight = PrintTrueFontW(nPositionX, nPositionY, TEXT("Arial"), 10, TEXT("Time: 12:30:45"), FALSE, 0, TRUE);

	End_Page();	// End Page
	End_Doc();	// End Document
}

void CSamplePg_VCDlg::OnBnClickedCashdrawerOpen()
{
	int			nPositionX	= 0;	
	int			nPositionY	= 0;
	int			nTextHeight	= 0;
	CString		strBuffer	= TEXT("");

	UpdateData(TRUE);

	// Start Document
	if(Start_DocW(TEXT("Open CashDrawer"))) 
	{
		// Start Page
		Start_Page();

		switch(m_cmbCashdrawer_Speed.GetCurSel()) 
		{
		case SPEED_50MS:	strBuffer.Format(TEXT("a"));	break;
		case SPEED_100MS:	strBuffer.Format(TEXT("b"));	break;
		case SPEED_150MS:	strBuffer.Format(TEXT("c"));	break;
		case SPEED_200MS:	strBuffer.Format(TEXT("d"));	break;
		case SPEED_250MS:	strBuffer.Format(TEXT("e"));	break;
		default:			strBuffer.Format(TEXT("f"));	break;
		}

		if(((CButton*)GetDlgItem(IDC_RADIO_CASHDRAWER_1))->GetCheck() )
			strBuffer.MakeUpper();
		else if(((CButton*)GetDlgItem(IDC_RADIO_CASHDRAWER_2))->GetCheck() )
			strBuffer.MakeLower();

		nPositionY += nTextHeight;
		nTextHeight = PrintDeviceFontW(nPositionX, nPositionY, TEXT("FontControl"), 0, strBuffer.GetBuffer(strBuffer.GetLength()));

		End_Page();	// End Page
		End_Doc();	// End Document
	}

}

void CSamplePg_VCDlg::OnBnClickedCancel()
{
	OnCancel();
}
