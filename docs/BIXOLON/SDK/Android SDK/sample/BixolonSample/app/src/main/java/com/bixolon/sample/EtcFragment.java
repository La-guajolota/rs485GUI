package com.bixolon.sample;

import android.app.AlertDialog;
import android.content.ContentResolver;
import android.content.DialogInterface;
import android.content.Intent;
import android.database.Cursor;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.net.Uri;
import android.os.Bundle;
import android.os.Environment;
import android.provider.MediaStore;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Toast;

import com.bixolon.sample.PrinterControl.BixolonPrinter;

import java.io.File;
import java.io.FileFilter;
import java.text.NumberFormat;

public class EtcFragment extends Fragment implements View.OnClickListener {
    private int REQUEST_CODE_ACTION_PICK = 1;

    private String[] fileList = null;;

    public static EtcFragment newInstance() {
        EtcFragment fragment = new EtcFragment();
        Bundle args = new Bundle();
        fragment.setArguments(args);
        return fragment;
    }

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fragment_etc, container, false);

        view.findViewById(R.id.buttonCutPaper).setOnClickListener(this);
        view.findViewById(R.id.buttonFormFeed).setOnClickListener(this);
        view.findViewById(R.id.buttonTransactionPrint).setOnClickListener(this);
        view.findViewById(R.id.buttonReceiptSample).setOnClickListener(this);
        view.findViewById(R.id.buttonPrintNVImage).setOnClickListener(this);
        view.findViewById(R.id.buttonCheckHealth).setOnClickListener(this);
        view.findViewById(R.id.buttonInfo).setOnClickListener(this);
        view.findViewById(R.id.buttonFarsiSample).setOnClickListener(this);
        view.findViewById(R.id.buttonFarsiSample).setEnabled(false);
        view.findViewById(R.id.buttonLocalCardInfo).setOnClickListener(this);
        view.findViewById(R.id.buttonUpdateFirmware).setOnClickListener(this);

        return view;
    }

    @Override
    public void onClick(View view) {
        switch (view.getId()) {
            case R.id.buttonCutPaper:
                MainActivity.getPrinterInstance().cutPaper();
                break;
            case R.id.buttonFormFeed:
                MainActivity.getPrinterInstance().formFeed();
                break;
            case R.id.buttonTransactionPrint:
                transactionPrint();
                break;
            case R.id.buttonReceiptSample:
                receiptSample();
                break;
            case R.id.buttonPrintNVImage:
                showGallery();
                break;
            case R.id.buttonCheckHealth:
                String checkHealth = MainActivity.getPrinterInstance().posPrinterCheckHealth();
                if (checkHealth != null) {
                    Toast.makeText(getContext(), checkHealth, Toast.LENGTH_LONG).show();
                }
                break;
            case R.id.buttonInfo:
                String info = MainActivity.getPrinterInstance().getPosPrinterInfo();
                if (info != null) {
                    Toast.makeText(getContext(), info, Toast.LENGTH_LONG).show();
                }
                break;
            case R.id.buttonFarsiSample:
                farsiSample();
                break;
            case R.id.buttonLocalCardInfo:
                getLocalCardInfo();
                break;
            case R.id.buttonUpdateFirmware:
                showFirmwareFileList();
        }
    }

    private void transactionPrint() {
        MainActivity.getPrinterInstance().beginTransactionPrint();

        MainActivity.getPrinterInstance().printText("Transaction mode\n", 0, 0, 1);
        Bitmap bitmap = BitmapFactory.decodeResource(getResources(), R.drawable.bixolonlogo);
        MainActivity.getPrinterInstance().printImage(bitmap, 250, MainActivity.getPrinterInstance().ALIGNMENT_CENTER, 65);
        MainActivity.getPrinterInstance().printBarcode("123456789012", MainActivity.getPrinterInstance().BARCODE_TYPE_ITF, 3, 150, 2, MainActivity.getPrinterInstance().BARCODE_HRI_BELOW);

        MainActivity.getPrinterInstance().endTransactionPrint();
    }

    private void receiptSample() {
        MainActivity.getPrinterInstance().beginTransactionPrint();

        String data = "";
        data = "Comp: TICKET\n" +
                "Walton, KT12 3BS\n" +
                "Tel: 01932 901 155\n" +
                "123-456-789\n" +
                "VAT No. 123456789\n\n";
        MainActivity.getPrinterInstance().printText("TICKET\n\n", BixolonPrinter.ALIGNMENT_CENTER, BixolonPrinter.ATTRIBUTE_BOLD | BixolonPrinter.ATTRIBUTE_UNDERLINE, 2);
        MainActivity.getPrinterInstance().printBarcode("www.bixolon.com", BixolonPrinter.BARCODE_TYPE_QRCODE, 8, 8, BixolonPrinter.ALIGNMENT_CENTER, BixolonPrinter.BARCODE_HRI_NONE);
        MainActivity.getPrinterInstance().printText(data, BixolonPrinter.ALIGNMENT_CENTER, BixolonPrinter.ATTRIBUTE_BOLD, 1);
        MainActivity.getPrinterInstance().printText("Sale:       " + "19-05-2017 16:19:43\n", BixolonPrinter.ALIGNMENT_LEFT, BixolonPrinter.ATTRIBUTE_BOLD, 1);

        data = "Gate:       " + "Xcover kiosk\n" +
                "Operator:   " + "Rob\n" +
                "Order Code: " + "263036991\n";
        MainActivity.getPrinterInstance().printText(data, BixolonPrinter.ALIGNMENT_LEFT, 0, 1);
        MainActivity.getPrinterInstance().printText("Qty Price  Item     Total\n", BixolonPrinter.ALIGNMENT_LEFT, BixolonPrinter.ATTRIBUTE_UNDERLINE, 1);
        MainActivity.getPrinterInstance().printText(" 1  $8.00  PARKING  $8.00\n", BixolonPrinter.ALIGNMENT_LEFT, 0, 1);

        data = "Total (inc VAT):  " + "  $8.00\n" +
                "VAT amount (20%): " + "  $1.33\n" +
                "CARD payment:     " + "  $8.00\n" +
                "Change due:       " + "  $0.00\n\n";
        MainActivity.getPrinterInstance().printText(data, BixolonPrinter.ALIGNMENT_RIGHT, BixolonPrinter.ATTRIBUTE_NORMAL, 1);

        data = "Thank you for your purchase!\n" +
                "Enjoy the show!\n" +
                "Next year visit\n" +
                "www.bixolon.com\n" +
                "to buy discounted tickets.\n\n\n\n";
        MainActivity.getPrinterInstance().printText(data, BixolonPrinter.ALIGNMENT_CENTER, BixolonPrinter.ATTRIBUTE_BOLD, 1);

        MainActivity.getPrinterInstance().endTransactionPrint();
    }

    private void farsiSample() {
        int currentCs = MainActivity.getPrinterInstance().getCharacterSet();

        MainActivity.getPrinterInstance().setCharacterSet(BixolonPrinter.CS_FARSI);

        // Farsi option : Mixed
        MainActivity.getPrinterInstance().setFarsiOption(BixolonPrinter.OPT_REORDER_FARSI_MIXED);
        printReceiptforFarsi();

        // Farsi option : Right to Left
        MainActivity.getPrinterInstance().setFarsiOption(BixolonPrinter.OPT_REORDER_FARSI_RTL);
        printReceiptforFarsi();

        MainActivity.getPrinterInstance().setCharacterSet(currentCs);
    }

    private void printReceiptforFarsi() {

        String printText = "A. 1. عدد ۰۱۲۳۴۵۶۷۸۹" + "\nB. 2. عدد 0123456789" + "\nC. 3. به" + "\nD. 4. نه" + "\nE. 5. مراجعه" + "\n۱۳۹۷/۰۸/۱۱";

        MainActivity.getPrinterInstance().printText(printText, BixolonPrinter.ALIGNMENT_RIGHT, 0, 1);

        String address = "";
        address = "\nBIXOLON شرکت با مسئولیت محدود . 7 FL،";
        address += "\nMiraeAsset سرمایه گذاری برج 685 ،";
        address += "\nSampyeong دونگ، Bundang گو ، سئونگنام - سی،";
        address += "\nگیونگی-دو ، 463-400 ، کره";
        MainActivity.getPrinterInstance().printText("\n" + address, BixolonPrinter.ALIGNMENT_RIGHT, 0, 1);
    }

    private void getLocalCardInfo() {
        if (MainActivity.getPrinterInstance().localSmartCardRWOpen()) {
            if (MainActivity.getPrinterInstance().getLocalCardInfo(10)) {
                byte[] track2 = MainActivity.getPrinterInstance().getLocalTrack2();
                byte[] cardNumber = MainActivity.getPrinterInstance().getLocalCardNumber();
                byte[] cardDueDate = MainActivity.getPrinterInstance().getLocalCardDueDate();

                String msg = "";
                if (track2 != null || track2.length > 0) {
                    msg = "Track2 : ";
                    for(int i = 0; i < track2.length; i++)  msg += String.format("%02X ", track2[i]);
                    msg += "\n";
                }

                if (cardNumber != null && cardDueDate != null) {
                    msg += (("Card Number : " + new String(cardNumber) + "\n") +
                            ("Card Due Date : " + new String(cardDueDate)));

                    Toast.makeText(getContext(), msg, Toast.LENGTH_LONG).show();
                }
            }

            MainActivity.getPrinterInstance().localSmartCardRWClose();
        }
    }

    private void showGallery() {
        String externalStorageState = Environment.getExternalStorageState();

        if (externalStorageState.equals(Environment.MEDIA_MOUNTED)) {
            Intent intent = new Intent(Intent.ACTION_PICK);
            intent.setType(android.provider.MediaStore.Images.Media.CONTENT_TYPE);
            startActivityForResult(intent, REQUEST_CODE_ACTION_PICK);
        }
    }

    private void showFirmwareFileList() {
        String PATH = Environment.getExternalStorageDirectory().getAbsolutePath();

        File file = new File(PATH);
        File[] files = file.listFiles(new FileFilter() {
            @Override
            public boolean accept(File pathname) {
                if (pathname.isDirectory()) {
                    return false;
                }

                String name = pathname.getName();
                int lastIndex = name.lastIndexOf('.');
                if (lastIndex < 0) {
                    return false;
                }

                if (name.substring(lastIndex).equalsIgnoreCase(".fls") ||
                        name.substring(lastIndex).equalsIgnoreCase(".bin")) {
                    return true;
                }

                return false;
            }
        });

        if (files != null && files.length > 0) {
            fileList = null;
            fileList = new String[files.length];
            for (int i = 0; i < fileList.length; i++) {
                fileList[i] = files[i].getAbsolutePath();
            }

            AlertDialog dialog = new AlertDialog.Builder(getContext()).setTitle("PDF List").setItems(fileList, new DialogInterface.OnClickListener() {
                public void onClick(DialogInterface dialog, int which) {
                    MainActivity.getPrinterInstance().updateFirmware(fileList[which]);
                }
            }).create();
            dialog.show();
        } else {
            Toast.makeText(getContext(), "No PDF file", Toast.LENGTH_SHORT).show();
        }
    }

    @Override
    public void onActivityResult(int requestCode, int resultCode, Intent data) {
        if (requestCode == REQUEST_CODE_ACTION_PICK) {
            if (data != null) {
                Uri uri = data.getData();
                ContentResolver cr = getActivity().getContentResolver();
                Cursor c = cr.query(uri, new String[]{MediaStore.Images.Media.DATA}, null, null, null);
                if (c == null || c.getCount() == 0) {
                    return;
                }

                c.moveToFirst();
                int columnIndex = c.getColumnIndexOrThrow(MediaStore.Images.Media.DATA);
                String text = c.getString(columnIndex);

                int width = MainActivity.getPrinterInstance().getPrinterMaxWidth();
                if (MainActivity.getPrinterInstance().defineNvImage(text, 1, 200, 50)) {
                    MainActivity.getPrinterInstance().printNVImage(1);
                }
            }
        }
    }
}
