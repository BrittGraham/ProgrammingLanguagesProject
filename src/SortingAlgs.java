import java.time.Duration;
import java.time.Instant;
import java.util.Arrays;
import java.util.Random;

public class SortingAlgs {
    public static void main(String[] args) {
        System.out.println("Random Array:");
        int[] x = generateArray();
        int[] forSS = x;
        int[] forBS = x;
        int[] forMS = x;
        int[] forQS = x;
        long selectionSortTime = selectionSort(forSS, forSS.length);
        long bubbleSortTime = BubbleSort(forBS,forBS.length);
        long mergeSortTime = mergeSort(x,0, (x.length -1));
        long quickSortTime = quickSort(x, 0, (x.length-1));
        System.out.println("-------------------------------");
        System.out.println("New order using Selection Sort:");
        System.out.println(Arrays.toString(forSS));
        System.out.println("Time to complete: " + selectionSortTime + " Milliseconds");
        System.out.println("Total lines of code: 10");
        System.out.println("");
        System.out.println("New order using Bubble Sort:");
        System.out.println(Arrays.toString(forBS));
        System.out.println("Time to complete: " + bubbleSortTime + " Milliseconds");
        System.out.println("Total lines of code: 4");
        System.out.println("");
        System.out.println("New order using Merge Sort:");
        System.out.println(Arrays.toString(forMS));
        System.out.println("Time to complete: " + mergeSortTime + " Milliseconds");
        System.out.println("Total lines of code: 33");
        System.out.println("");
        System.out.println("New order using Quick Sort:");
        System.out.println(Arrays.toString(forQS));
        System.out.println("Time to complete: " + quickSortTime + " Milliseconds");
        System.out.println("Total lines of code: 18");
        System.out.println("");
    }

    public static int[] generateArray(){
        Random random = new Random();
        int[] array = new int[1000];
        for(int i = 0; i < array.length; i++){
            array[i] = (random.nextInt())%1000;
        }
        System.out.println(Arrays.toString(array));
        return array;
    }
    
    //Selection sort
    private static long selectionSort(int[] A, int n) {
        Instant start = Instant.now();
        for (int i = 0; i < n - 1; i++) {
            int first = i;
            int minimum = first;
            for (int j = i + 1; j < n; j++) {
                if (A[j] < A[minimum]) {
                    minimum = j;
                }
            }
            if (minimum != first) {
                int temp = A[minimum];
                A[minimum] = A[i];
                A[i] = temp;
            }
        }
        Instant end = Instant.now();
        return Duration.between(start, end).toMillis();
    }

    //Bubble sort
    private static long BubbleSort(int[] A, int n) {
        Instant start = Instant.now();
        for(int i = 0; i < n; i++) {
            for(int j = 1; j < (n - i); j++) {
                if(A[j-1] > A[j]) {
                    int temp = A[j-1];A[j-1] = A[j];A[j] = temp;
                }
            }
        }
        Instant end = Instant.now();
        return Duration.between(start, end).toMillis();
    }

    //merge sort
    private static long mergeSort(int[] A, int low, int high) {
        Instant start = Instant.now();
        if(low < high){
            int middle = (int)(Math.floor((low + high)/2));
            mergeSort(A, low, middle);
            mergeSort(A, middle+1, high);
            merge(A, low, middle, high);
        }
        Instant end = Instant.now();
        return Duration.between(start, end).toMillis();
    }

    //merge sort part 2. This merges the two arrays together into one array.
    private static void merge(int A[], int low, int mid, int high) {
        int[] b = new int[(mid-low) + 1];
        int[] c = new int[(high - mid)];
        for (int i = 0; i < b.length; i ++) {
            b[i] = A[low + i];
        }
        for (int j = 0; j < c.length; j++) {
            c[j] = A[(mid+1) + j];
        }
        int k = low;
        int i = 0;
        int j = 0;
        while(i < b.length && j < c.length) {
            if(b[i] < c[j]){
                A[k] = b[i];
                i++;
                k++;
            }
            else{
                A[k] = c[j];
                j++;
                k++;
            }
        }
        if( i == b.length) {
            while(j < c.length) {
                A[k] = c[j];
                j++;
                k++;
            }
        }
        else{
            while(i < b.length) {
                A[k] = b[i];
                i++;
                k++;
            }
        }
    }


    //Quick sort
    private static long quickSort(int[] A, int low, int high) {
        Instant start = Instant.now();
        if( low > high) {
            return 0;
        }
        else {
            int i = partition(A, low, high);
            quickSort(A, low, i-1);
            quickSort(A, i+1, high);
        }
        Instant end = Instant.now();
        return Duration.between(start, end).toMillis();
    }

    private static int partition(int[] A, int low, int high) {
        int pivot = A[high];
        int i = low - 1;
        for(int j = low; j <= high - 1; j++) {
            if(A[j] <= pivot) {
                i++;
                int temp = A[i];
                A[i] = A[j];
                A[j] = temp;
            }
        }
        int temp = A[i + 1];
        A[i + 1] = A[high];
        A[high] = temp;
        return i + 1;
    }

}
