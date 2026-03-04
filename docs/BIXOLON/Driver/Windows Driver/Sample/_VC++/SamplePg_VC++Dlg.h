
// SamplePg_VC++Dlg.h : header file
//

#pragma once
#include "afxwin.h"


// CSamplePg_VCDlg dialog
class CSamplePg_VCDlg : public CDialog
{
// Construction
public:
	CSamplePg_VCDlg(CWnd* pParent = NULL);	// standard constructor

// Dialog Data
	enum { IDD = IDD_SAMPLEPG_VC_DIALOG };

	protected:
	virtual void DoDataExchange(CDataExchange* pDX);	// DDX/DDV support

	void EnableCtrls(BOOL bConnect);

// Implementation
protected:
	HICON m_hIcon;

	// Generated message map functions
	virtual BOOL OnInitDialog();
	afx_msg void OnPaint();
	afx_msg HCURSOR OnQueryDragIcon();
	DECLARE_MESSAGE_MAP()

protected:
	afx_msg void OnBnClickedConnect();
	afx_msg void OnBnClickedDisconnect();
	afx_msg void OnBnClickedPrintDevicefont();
	afx_msg void OnDestroy();

	CComboBox m_cmbDeviceFont;

	CString m_strPrinterName;
	CComboBox m_cmbCashdrawer_Speed;
public:
	afx_msg void OnBnClickedPartialcut();
	afx_msg void OnBnClickedPartialcutNofeed();
	afx_msg void OnBnClickedPrintReceipt();
	afx_msg void OnBnClickedCancel();
	afx_msg void OnBnClickedCashdrawerOpen();
};
